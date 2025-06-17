# app.py  –  HR Copilot (4‑Agent, Gemini‑Only, Key‑in‑Sidebar)

import os
import streamlit as st

# LangChain bits
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain_google_genai import GoogleGenerativeAIEmbeddings  
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Set Gemini API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyATxu5mFwegMrmPw0X0rb88b1wf40xR-jM"


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
# ------------------------------------------------------------------
# 0️⃣  STREAMLIT CONFIG + KEY INPUT
# ------------------------------------------------------------------
st.set_page_config("HR Copilot - 4-Agent Edition", layout="centered")
st.title("🤖 HR Copilot")
st.caption("Ask HR stuff like you would in Slack. I'll do the boring bits.")

# Sidebar prompt for the Gemini key (masked)
api_key = st.sidebar.text_input(
    "🔑 Enter your Google Gemini API key", type="password", placeholder="Paste key here"
)

if not api_key:
    st.stop("⏹️  Paste your API key in the sidebar to start.")

os.environ["GOOGLE_API_KEY"] = api_key  # shove it into env so LangChain can see it

# ------------------------------------------------------------------
# 1️⃣  MODELS & RAG BACKEND
# ------------------------------------------------------------------
llm = ChatGoogleGenerativeAI(model="gemini-2.0-Flash", google_api_key=api_key)
embedder = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)

@st.cache_resource(show_spinner="📚 Indexing HR policy docs…")
def _build_retriever(path="docs/hr_policies.pdf"):
    loader = PyPDFLoader(path)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
    chunks = splitter.split_documents(pages)
    vs = FAISS.from_documents(chunks, embedder)
    return vs.as_retriever(search_kwargs={"k": 4})

retriever = _build_retriever()
qa_chain  = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# ------------------------------------------------------------------
# 2️⃣  AGENT CLASSES
# ------------------------------------------------------------------
class IntentClassifierAgent:
    MAP = {
        "leave": ["leave", "vacation", "holiday", "day off"],
        "payslip": ["payslip", "salary", "payment", "compensation"],
        "appraisal": ["appraisal", "review", "performance"],
        "mental_health": ["mental", "stress", "burnout", "depression"],
    }
    def run(self, text: str) -> str:
        low = text.lower()
        for label, words in self.MAP.items():
            if any(w in low for w in words):
                return label
        return "general"

class RetrieverAgent:
    def run(self, q: str) -> str:
        return qa_chain.run(q)

class ActionAgent:
    ACTIONS = {
        "leave": "📨 Leave form emailed. Fill it out and chill.",
        "payslip": "📨 Latest payslip dropped in your inbox.",
        "appraisal": "🔔 Appraisal reminder pinged to you and the boss.",
    }
    def run(self, intent: str) -> str:
        return self.ACTIONS.get(intent, " No automated action for that request.")

class EscalationAgent:
    def run(self, intent: str) -> bool:
        return intent == "mental_health"

intent_agent   = IntentClassifierAgent()
retriever_agent = RetrieverAgent()
action_agent   = ActionAgent()
escalate_agent = EscalationAgent()

# ------------------------------------------------------------------
# 3️⃣  MAIN CHAT PIPELINE
# ------------------------------------------------------------------
q = st.text_input("💬 Your message", placeholder="e.g. 'I need my payslip for April'")
if not q:
    st.stop()

intent = intent_agent.run(q)
st.markdown(f"**🎯 Intent:** `{intent}`")

if escalate_agent.run(intent):
    st.error("🚨 Sensitive topic detected. Escalating to a human HR pro.")
    st.stop()

policy_info = retriever_agent.run(q)
st.markdown("**📄 Policy says:**")
st.write(policy_info)

action_msg = action_agent.run(intent)
st.success(action_msg)
from langchain.document_loaders import PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader
from langchain.document_loaders import UnstructuredFileLoader
import tempfile

# --------------------------
# 🆕 File Uploader UI
# --------------------------
st.subheader("📁 Upload HR Policy Document")
uploaded_file = st.file_uploader("Upload a PDF, TXT, or DOCX file", type=["pdf", "txt", "docx"])

if not uploaded_file:
    st.stop("📎 Upload an HR document to begin.")

# --------------------------
# 🧠 Dynamic Retriever Builder
# --------------------------
@st.cache_resource(show_spinner="📚 Indexing uploaded document…")
def _build_dynamic_retriever(file):
    # Save to temp file
    suffix = "." + file.name.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name

    # Pick loader
    if suffix == ".pdf":
        loader = PyPDFLoader(tmp_path)
    elif suffix == ".txt":
        loader = TextLoader(tmp_path)
    elif suffix == ".docx":
        loader = UnstructuredWordDocumentLoader(tmp_path)
    else:
        st.error("❌ Unsupported file type.")
        st.stop()

    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    vectordb = FAISS.from_documents(chunks, embedder)
    return vectordb.as_retriever(search_kwargs={"k": 4})

retriever = _build_dynamic_retriever(uploaded_file)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
import streamlit as st

def stop(_=None):
    st.write("Stop clicked!")

st.button("Stop", on_click=stop)
