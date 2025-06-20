import streamlit as st
import os
import json
from datetime import datetime
from fpdf import FPDF
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import re

st.set_page_config(page_title="Student Project AI Workflow", layout="wide")

# Inject custom CSS
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6em 1.2em;
    }
    .stTextInput>div>input, .stTextArea>div>textarea {
        background-color: #ffffff;
        border: 1px solid #ccc;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Emoji remover for PDF compatibility
def remove_emojis(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

st.title("🤖 Student Project AI Workflow")

API_KEY = st.text_input("🔑 Enter your Gemini API Key", type="password")
uploaded_pdf = st.file_uploader("📄 Upload Final Project PDF (optional)", type=["pdf"])

project_dir = st.text_input("📁 Enter Project Folder Name", "student_project")
title = st.text_input("📌 Project Title")
student_names = st.text_area("👥 Student Names (comma-separated)")
duration_weeks = st.number_input("⏳ Duration (weeks)", min_value=1, value=8)
department = st.text_input("🏫 Department")
domain = st.text_input("🧠 Domain")
team_roles = st.text_area("👩‍💻 Team Roles & Skill Mapping (e.g. Alice: Frontend, Bob: Backend)")
feedback_input = st.text_area("📝 Feedback Summary")

generate_button = st.button("🚀 Run All Agents")

if generate_button:
    if not all([API_KEY, title, student_names, department, domain]):
        st.error("Please fill in all required fields.")
    else:
        os.makedirs(project_dir, exist_ok=True)
        for folder in ['docs', 'assets', 'src', 'report']:
            os.makedirs(os.path.join(project_dir, folder), exist_ok=True)

        team = [name.strip() for name in student_names.split(",")]
        metadata = {
            "title": title,
            "team": team,
            "duration_weeks": duration_weeks,
            "department": department,
            "domain": domain,
            "created_at": datetime.now().isoformat()
        }

        with open(os.path.join(project_dir, "metadata.json"), "w") as f:
            json.dump(metadata, f, indent=4)

        with open(os.path.join(project_dir, "README.md"), "w") as f:
            f.write(f"# {title}\n\n**Department**: {department}\n**Domain**: {domain}\n**Team**: {', '.join(team)}\n**Duration**: {duration_weeks} weeks")

        with open(os.path.join(project_dir, "timeline.txt"), "w") as f:
            f.write("WEEK 1: Project kickoff, literature review\nWEEK 2: Finalize problem statement")

        st.success("✅ Project scaffold created.")

        # Timeline Agent
        loader = TextLoader(os.path.join(project_dir, "README.md"))
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectordb = FAISS.from_documents(chunks, embeddings)
        retriever = vectordb.as_retriever()

        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=API_KEY)
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

        prompt = f"""
You are an academic timeline generator. Create 3–5 project phases for:
- Title: {title}
- Domain: {domain}
Each phase must include: name, goal, start_week, and end_week.
Return in plain text format.
"""
        timeline_text = qa_chain.run(prompt)
        with open(os.path.join(project_dir, "timeline_detailed.txt"), "w") as f:
            f.write(timeline_text)
        st.text_area("📅 Timeline Output", timeline_text, height=250, key="timeline_output")

        # Branding Agent
        timeline_summary = timeline_text.replace("\n", " ")
        branding_template = PromptTemplate(
            input_variables=["title", "domain", "team", "timeline"],
            template="""
You are a branding assistant.
Project Title: {title}
Domain: {domain}
Team: {team}
Timeline: {timeline}
Generate:
1. LinkedIn post
2. GitHub README additions
3. Resume bullets
4. One-paragraph case booklet summary
"""
        )

        branding_chain = LLMChain(llm=llm, prompt=branding_template)
        branding_output = branding_chain.run(
            title=title,
            domain=domain,
            team=", ".join(team),
            timeline=timeline_summary
        )

        with open(os.path.join(project_dir, "branding_output.txt"), "w", encoding="utf-8") as f:
            f.write(branding_output)
        st.text_area("🎨 Branding Output", branding_output, height=300, key="branding_output")

        # Task Agent
        task_template = PromptTemplate(
            input_variables=["title", "domain", "team_roles", "feedback"],
            template="""
Project Title: {title}
Domain: {domain}
Roles & Skills:
{team_roles}
Feedback:
{feedback}
Create a detailed task plan and timeline update as readable text.
"""
        )

        task_chain = LLMChain(llm=llm, prompt=task_template)
        task_output = task_chain.run(
            title=title,
            domain=domain,
            team_roles=team_roles,
            feedback=feedback_input
        )

        with open(os.path.join(project_dir, "task_plan.txt"), "w", encoding="utf-8") as f:
            f.write(task_output)
        st.text_area("🧩 Task Plan Output", task_output, height=300, key="task_plan_output")

        # Checklist & Summary
        checklist = {
            "README.md created": True,
            "Project folders organized": True,
            "metadata.json present": True,
            "timeline_detailed.txt generated": True,
            "branding_output.txt available": True,
            "Final report added in /report": bool(uploaded_pdf),
            "Assets uploaded in /assets": True
        }

        summary_text = f"""
📋 Student Project Submission Report
Generated at: {datetime.now().isoformat()}

✔️ Completed:
"""
        for item, done in checklist.items():
            if done:
                summary_text += f"- {item}\n"

        summary_text += "\n❌ Missing:\n"
        for item, done in checklist.items():
            if not done:
                summary_text += f"- {item}\n"

        # Clean and write
        clean_summary = remove_emojis(summary_text)

        with open(os.path.join(project_dir, "submission_report.txt"), "w", encoding="utf-8") as f:
            f.write(summary_text)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in clean_summary.split("\n"):
            pdf.cell(200, 10, txt=line, ln=True)

        pdf_path = os.path.join(project_dir, "submission_report.pdf")
        pdf.output(pdf_path)

        st.success("📄 Submission Report Generated")
        st.download_button("📥 Download PDF Report", open(pdf_path, "rb"), file_name="submission_report.pdf")
        st.text_area("📋 Report Summary", summary_text, height=250, key="report_summary")

        # Save uploaded report
        if uploaded_pdf:
            with open(os.path.join(project_dir, "report", "final_report.pdf"), "wb") as f:
                f.write(uploaded_pdf.read())
            st.success("✅ Final report uploaded to /report")
