# Student Project AI Workflow

**Department**: [Department Name]  
**Domain**: [Project Domain]  
**Team**: [Alice, Bob, Charlie]  
**Duration**: 8 weeks

## 📌 Overview

This AI-powered Streamlit app helps automate the complete lifecycle of a student project. It enables generation of:
- Project folder scaffolding
- AI-generated academic timeline
- Branding content (LinkedIn, GitHub, Resume lines, Case booklet)
- Detailed task plan based on team roles and feedback
- Project submission report (PDF)
- Option to upload final report

## 🚀 Features

- 🧠 Uses Google Gemini 2.0 Flash for intelligent generation
- 🛠️ Agents for Timeline, Branding, and Task planning
- 📁 Automatically organizes project assets and metadata
- 📄 Exports a professional submission summary report (PDF)
- ✅ Supports uploading and saving the final project PDF

## 🧩 Tech Stack

- **Frontend**: Streamlit
- **LLM**: Google Gemini 2.0 Flash (`langchain_google_genai`)
- **Vector Store**: FAISS
- **Embeddings**: all-MiniLM-L6-v2 (`HuggingFaceEmbeddings`)
- **PDF Generator**: FPDF


## 🧪 How to Run

1. Clone this repo or copy the `app.py` file into your Streamlit project.
2. Install dependencies:
    ```bash
    pip install streamlit langchain fpdf faiss-cpu transformers
    ```
3. Run the app:
    ```bash
    streamlit run app.py
    ```
4. Enter your [Google Gemini API key](https://makersuite.google.com/app/apikey) in the UI.

## 📥 Output Files

- `timeline_detailed.txt`: Timeline phases (AI-generated)
- `branding_output.txt`: LinkedIn/GitHub/Resume content
- `task_plan.txt`: Detailed task planning
- `submission_report.pdf`: Final submission summary

## 📌 Future Enhancements

- Integrate feedback loop with faculty
- Add email notifications
- Deploy as a hosted web app for institution-wide use


