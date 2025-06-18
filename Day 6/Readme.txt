import streamlit as st
import re
import os
from datetime import datetime, timedelta
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# === Set Page Config (Must be the first Streamlit command) ===
st.set_page_config(page_title="HR Copilot", layout="wide")

# Simulated HR Policy Data (since we can't access real PDFs/Google Docs)
HR_POLICIES = {
    "leave": """
    *Leave Policy*  
    - Annual Leave: 20 days per year, accrued monthly.  
    - Sick Leave: 10 days per year, fully paid.  
    - Maternity/Paternity Leave: 12 weeks, fully paid.  
    - Unpaid Leave: Available upon approval for up to 30 days.  
    To apply, submit a request via the HR portal at least 5 days in advance.
    """,
    "appraisal": """
    *Appraisal Policy*  
    - Appraisals occur bi-annually: June and December.  
    - Employees must submit a self-assessment form 2 weeks prior.  
    - Managers will schedule a 1:1 review meeting post-submission.  
    Contact HR if you haven't received your appraisal form.
    """,
    "payslip": """
    *Payslip Information*  
    - Payslips are issued on the last working day of each month.  
    - Access your payslip via the HR portal under 'Payroll'.  
    - For discrepancies, email hr@company.com with your employee ID.
    """
}

# Sensitive topics for escalation (used for double-checking in code)
SENSITIVE_TOPICS = ["mental health", "harassment", "discrimination"]

# === API Key Input Section ===
st.subheader("API Key Configuration")
google_api_key = st.text_input("Enter Google API Key", type="password", help="Enter your Google Generative AI API Key")

# Set API Key in environment variable if provided
if google_api_key:
    os.environ["GOOGLE_API_KEY"] = google_api_key

# Validate API Key
if not os.environ.get("GOOGLE_API_KEY"):
    st.error("❌ Please provide a Google API Key to proceed.")
    st.stop()

# Initialize Gemini API with LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.3,
    max_output_tokens=1024
)

# LangChain Prompt for Intent Classification and Response Generation
hr_prompt = ChatPromptTemplate.from_template("""
You are an HR Copilot designed to assist employees with common HR queries and tasks. Based on the user's query, perform the following:

1. *Classify Intent*: Identify the intent of the query. Possible intents include:
   - leave (queries about leave policies)
   - appraisal (queries about appraisals or performance reviews)
   - payslip (queries about salary or payslips)
   - interview (queries about scheduling interviews)
   - escalate (queries containing sensitive topics like 'mental health', 'harassment', or 'discrimination')
   - unknown (if the intent is unclear)

2. *Fetch Answer*: If the intent is 'leave', 'appraisal', or 'payslip', use the following HR policy data to generate a response:
   *HR Policies*:
   {policy_data}

3. *Trigger Action*: If applicable, suggest a mock action based on the intent:
   - For 'appraisal', suggest sending a reminder for form submission (e.g., due tomorrow).
   - For 'interview', suggest scheduling an interview slot (e.g., in 3 days at 10:00 AM).

4. *Escalation Check*: If the intent is 'escalate', return a message indicating the query will be escalated to HR. Do not provide a policy answer or action.

*User Query*: {query}

*Output Format*:
- *Intent*: [intent]
- *Response*: [response text]
- *Action* (if applicable): [action text]
""")
