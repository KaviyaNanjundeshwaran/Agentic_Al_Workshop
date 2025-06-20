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


##My Output

 Student Project AI Workflow
🔑 Enter your Gemini API Key

•••••••••••••••••••••••••••••••••••••••

📄 Upload Final Project PDF (optional)

No file chosen
Drag and drop file here
Limit 200MB per file • PDF
📁 Enter Project Folder Name

student_project
📌 Project Title

Intelligent Script Analyzer
👥 Student Names (comma-separated)

 Aisha R, Karthik M, Neha S
⏳ Duration (weeks)

10


🏫 Department

Information Technology
🧠 Domain

AI Assisant
👩‍💻 Team Roles & Skill Mapping (e.g. Alice: Frontend, Bob: Backend)

 Aisha R: Frontend, Karthik M: Backend, Neha S: Designer
📝 Feedback Summary

Project Name: Intelligent Script Analyzer
Date: June 20, 2025
Reviewed By: AI Evaluation Agent

✅ Strengths
Innovative Concept: The idea of automating film/TV script evaluation with RAG and style guides is highly creative and fills a gap in the industry.

Multi-Agent Workflow: The use of LangGraph and multiple agents to handle scene, tone, and character breakdowns adds structure and scalability.

RAG Integration: Incorporating Retrieval-Augmented Generation ensures relevance and context-aware rewriting.

User Experience: The Streamlit interface is user-friendly and allows for manual file upload and API key entry, enhancing accessibility.

🛠️ Areas for Improvement
Error Handling: Some components lack fallback mechanisms when external services (e.g., Gemini API) fail or timeout.

Performance: Response time slows down with larger PDF scripts. Optimizing the chunking logic or vector retrieval may help.

UI Feedback: There’s minimal visual feedback when agents are executing. Adding a progress bar or stepwise indicator would improve UX.

💡 Suggestions
Add a logging feature for traceability and easier debugging.

Offer downloadable agent output in PDF or DOCX format.

Allow users to select different cinematic styles or writing tones dynamically.

🧠 Overall Impression
The system shows strong potential for transforming script writing and revision processes. With minor improvements, it could be production-ready for creative professionals and studios.

✅ Project scaffold created.

📅 Timeline Output

Okay, here's a possible project timeline for the "Intelligent Script Analyzer" project within the AI Assistant domain:

**Phase 1: Project Scoping and Data Acquisition**
*   **Goal**: Define project scope, gather initial data, and set up the development environment.
*   **Start Week**: 1
*   **End Week**: 2

**Phase 2: Core Analyzer Development**
*   **Goal**: Develop the core script analysis functionalities.
*   **Start Week**: 3
*   **End Week**: 6

**Phase 3: Testing and Refinement**
*   **Goal**: Test the analyzer, identify areas for improvement, and refine its accuracy.
*   **Start Week**: 7
*   **End Week**: 8

**Phase 4: Integration and Documentation**
*   **Goal**: Integrate the analyzer, and create project documentation.
*   **Start Week**: 9
*   **End Week**: 10
🎨 Branding Output

Okay, here's the content you requested, tailored to promote the "Intelligent Script Analyzer" project:

**1. LinkedIn Post**

**Option 1 (Focus on Impact):**

> Excited to share our team's project: the Intelligent Script Analyzer! 🤖 We built this AI-powered tool to help developers and content creators streamline their script analysis process. Built by Aisha R, Karthik M, and Neha S, this project uses cutting-edge AI to identify errors, suggest improvements, and enhance code readability. Check out the GitHub repo for more details and contribute to making scripting smarter! #AI #NLP #ScriptAnalysis #Python #OpenSource #Innovation #AIAssistant

**Option 2 (Focus on Timeline & Process):**

> Thrilled to announce the completion of our "Intelligent Script Analyzer" project! Over the past 10 weeks, Aisha R, Karthik M, and Neha S worked tirelessly to bring this AI-powered tool to life. From project scoping to final integration, we focused on creating a robust and user-friendly solution for script analysis. Key milestones included core analyzer development, rigorous testing, and comprehensive documentation. Learn more and contribute on GitHub! #AI #NLP #ProjectManagement #SoftwareDevelopment #AIAssistant

**2. GitHub README Additions**

```markdown
## Intelligent Script Analyzer

**An AI-powered tool for automated script analysis.**

**Project Overview:**

This project aims to provide developers and content creators with an intelligent tool to analyze scripts, identify potential errors, suggest improvements, and enhance readability. The analyzer leverages Natural Language Processing (NLP) and other AI techniques to provide comprehensive feedback.

**Key Features:**

*   **Error Detection:** Identifies common scripting errors.
*   **Style Suggestions:** Provides recommendations for code style and best practices.
*   **Readability Enhancement:** Offers suggestions to improve script clarity.
*   **Customizable Rules:** Allows users to define custom rules and guidelines for analysis.

**Project Timeline:**

*   **Phase 1: Project Scoping and Data Acquisition (Weeks 1-2)**
    *   Defined project scope, gathered initial data, and set up the development environment.
*   **Phase 2: Core Analyzer Development (Weeks 3-6)**
    *   Developed the core script analysis functionalities using NLP and AI techniques.
*   **Phase 3: Testing and Refinement (Weeks 7-8)**
    *   Tested the analyzer, identified areas for improvement, and refined its accuracy.
*   **Phase 4: Integration and Documentation (Weeks 9-10)**
    *   Integrated the analyzer, and created project documentation.

**Team:**

*   Aisha R
*   Karthik M
*   Neha S

**Contributing:**

We welcome contributions to this project! Please see the `CONTRIBUTING.md` file for guidelines on how to contribute.

**License:**

[Choose a License - e.g., MIT License]

```

**3. Resume Bullets (Tailored per Team Member - Example for Aisha R):**

*   **Led the project scoping and data acquisition phase for the "Intelligent Script Analyzer," an AI-powered tool designed to automate script analysis, resulting in a well-defined project scope and a robust dataset for training the AI model.**
*   **Developed key modules within the core analyzer, leveraging NLP techniques to identify scripting errors and suggest improvements, contributing to a [quantifiable result, e.g., 20%] improvement in script readability.**
*   **Collaborated with a team of three to integrate the analyzer, create comprehensive project documentation, and ensure the successful deployment of the tool.**

**(Repeat the above for Karthik M and Neha S, tailoring the bullets to their specific contributions.  Focus on action verbs and quantifiable results whenever possible.)**

**4. One-Paragraph Case Booklet Summary**

The Intelligent Script Analyzer is an AI-powered tool developed by Aisha R, Karthik M, and Neha S to streamline script analysis for developers and content creators. Utilizing NLP and machine learning techniques, the analyzer automatically identifies errors, suggests style improvements, and enhances overall script readability. Built over a 10-week period, the project encompassed data acquisition, core analyzer development, rigorous testing, and comprehensive documentation. This tool offers a significant advantage by automating a time-consuming task, enabling users to focus on more creative and strategic aspects of their work, and ultimately improving the quality and efficiency of script development.
🧩 Task Plan Output

Okay, here's a detailed task plan and timeline update based on the AI Evaluation Agent's feedback, presented in a readable format, designed for the Intelligent Script Analyzer project.  We'll focus on the areas for improvement and the suggestions, assigning tasks to the relevant team members (Aisha, Karthik, and Neha) and setting realistic deadlines.

**Project:** Intelligent Script Analyzer
**Date:** June 20, 2025
**Status:** Task Plan & Timeline Update (Based on AI Evaluation Agent Feedback)

**Overall Goal:** Enhance the Intelligent Script Analyzer to address identified weaknesses and implement suggested improvements, bringing it closer to production-readiness.

**Key Areas of Focus:**

*   Error Handling & Robustness
*   Performance Optimization
*   User Experience (UI/UX)
*   Additional Features (Logging, Downloadable Output, Style/Tone Selection)

**Task Breakdown & Timeline:**

**Phase 1: Error Handling & Logging (July 1st - July 15th)**

*   **Task 1.1: Implement Gemini API Fallback Mechanism (Karthik)**
    *   **Description:**  Create a robust error handling system for the Gemini API calls.  Implement retry logic with exponential backoff for temporary failures. If retries fail, provide a graceful error message to the user, suggesting alternative API keys or reporting a service outage.  Consider using a different API (e.g., GPT-4) as a last resort backup.
    *   **Deliverables:**  Code modifications with robust error handling, unit tests for error scenarios.
    *   **Deadline:** July 8th
    *   **Dependencies:**  Requires access to the Gemini API and knowledge of its error codes.
*   **Task 1.2: Implement System Logging (Karthik)**
    *   **Description:** Integrate a logging library (e.g., Python's `logging` module) to record key events, errors, and warnings throughout the application.  Log API calls, agent actions, and any exceptions that occur.  Configure the logging level (e.g., INFO, WARNING, ERROR) to control the verbosity of the logs.  Store logs in a file or database for later analysis.
    *   **Deliverables:**  Code modifications to add logging, configuration file for logging settings.
    *   **Deadline:** July 15th
    *   **Dependencies:**  Decision on logging framework and storage location.

**Phase 2: Performance Optimization (July 16th - July 31st)**

*   **Task 2.1: Optimize Chunking Logic (Karthik)**
    *   **Description:** Analyze the current PDF chunking strategy.  Experiment with different chunk sizes and overlap strategies to improve the speed and accuracy of the RAG system.  Consider using more sophisticated chunking methods that take into account sentence boundaries and semantic meaning.
    *   **Deliverables:**  Code modifications to optimize chunking, benchmark results showing improved performance.
    *   **Deadline:** July 22nd
    *   **Dependencies:**  Requires access to the PDF parsing library and the RAG system.
*   **Task 2.2: Optimize Vector Retrieval (Karthik)**
    *   **Description:** Investigate the performance of the vector retrieval process.  Explore different vector indexing techniques (e.g., HNSW, FAISS) to speed up the search.  Optimize the vector database configuration for faster queries.
    *   **Deliverables:**  Code modifications to optimize vector retrieval, benchmark results.
    *   **Deadline:** July 31st
    *   **Dependencies:**  Requires access to the vector database and knowledge of vector indexing techniques.

**Phase 3: UI/UX Enhancements (August 1st - August 15th)**

*   **Task 3.1: Implement Progress Bar/Stepwise Indicator (Aisha/Neha)**
    *   **Description:** Design and implement a progress bar or stepwise indicator to provide visual feedback to the user while the agents are executing.  The progress bar should reflect the overall progress of the analysis, as well as the progress of individual agents. Neha to design the visual elements and Aisha to implement it within Streamlit.
    *   **Deliverables:**  Modified Streamlit interface with progress bar/stepwise indicator.
    *   **Deadline:** August 8th
    *   **Dependencies:**  Requires knowledge of Streamlit and front-end development.
*   **Task 3.2: Implement Downloadable Output (Aisha/Karthik)**
    *   **Description:** Add functionality to allow users to download the agent output in PDF or DOCX format.  Karthik will handle the backend logic for generating the output files, and Aisha will create the download button in the Streamlit interface.
    *   **Deliverables:**  Code modifications to generate and download output files.
    *   **Deadline:** August 15th
    *   **Dependencies:**  Requires a library for generating PDF/DOCX files.

**Phase 4: Feature Enhancement (August 16th - August 31st)**

*   **Task 4.1: Dynamic Style/Tone Selection (Aisha/Karthik/Neha)**
    *   **Description:** Design and implement a feature that allows users to dynamically select different cinematic styles or writing tones for the rewriting process.  Neha will design the UI elements for selecting styles/tones, Karthik will handle the backend logic for applying the selected style/tone, and Aisha will integrate the feature into the Streamlit interface.
    *   **Deliverables:**  Modified Streamlit interface with style/tone selection, backend logic for applying styles/tones.
    *   **Deadline:** August 31st
    *   **Dependencies:**  Requires a database of cinematic styles and writing tones, and the ability to apply these styles/tones to the script.

**Team Responsibilities:**

*   **Aisha R (Frontend):** Streamlit interface development, UI/UX design implementation, integration of backend functionality.
*   **Karthik M (Backend):** API integration, error handling, performance optimization, logging, output file generation, style/tone application.
*   **Neha S (Designer):** UI/UX design for progress bar, style/tone selection.

**Communication:**

*   Daily stand-up meetings to discuss progress and any roadblocks.
*   Weekly project review meetings to track progress against the timeline and make adjustments as needed.
*   Use a project management tool (e.g., Asana, Jira) to track tasks and assign responsibilities.

**Success Metrics:**

*   Reduced error rates in API calls.
*   Improved response time for large PDF scripts.
*   Positive user feedback on the UI/UX enhancements.
*   Successful implementation of the new features.

This detailed task plan and timeline provides a roadmap for addressing the feedback from the AI Evaluation Agent and improving the Intelligent Script Analyzer. It's important to remain flexible and adjust the plan as needed based on progress and any new challenges that arise.  Good luck!
📄 Submission Report Generated
