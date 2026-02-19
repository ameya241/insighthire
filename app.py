import streamlit as st
import PyPDF2
from rag_pipeline import analyze_resume_vs_jd


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="InsightHire AI", layout="wide")

# -----------------------------
# Custom CSS Styling
# -----------------------------
st.markdown("""
    <style>
    body {
        background-color:#f2f5fa;
    }

    .main {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
    }

    h1 {
        text-align: center;
        color: #9c5c9c;
        font-weight: 800;
    }

    h2, h3 {
        color: #f8fafc;
    }

    .stButton>button {
        background: linear-gradient(90deg, #06b6d4, #3b82f6);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        height: 50px;
        width: 100%;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #3b82f6, #06b6d4);
    }

    .stTextArea textarea {
        background-color: #1e293b;
        color: white;
        border-radius: 10px;
    }

    .stFileUploader {
        background-color: #1e293b;
        border-radius: 10px;
        padding: 10px;
    }

    .css-1d391kg {
        background-color: #0f172a;
    }
    </style>
""", unsafe_allow_html=True)


# -----------------------------
# Title
# -----------------------------
st.title("🚀 InsightHire AI")
st.markdown("<h3 style='text-align: center;'>Resume vs Job Description Analyzer</h3>", unsafe_allow_html=True)


# -----------------------------
# Resume Upload
# -----------------------------
st.markdown("## 📄 Upload Resume (PDF)")
uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

resume_text = ""

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        resume_text += page.extract_text()


# -----------------------------
# Job Description
# -----------------------------
st.markdown("## 📝 Paste Job Description")
jd_text = st.text_area("Enter Job Description Here", height=200)


# -----------------------------
# Analyze
# -----------------------------
if resume_text and jd_text:

    if st.button("🔍 Analyze Match"):

        with st.spinner("Analyzing Resume vs JD..."):

            score, missing_keywords, matched_keywords = analyze_resume_vs_jd(resume_text, jd_text)

        st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #1e293b, #334155);
                padding: 25px;
                border-radius: 15px;
                text-align: center;
                margin-top: 20px;">
                <h2 style="color:#38bdf8;">🎯 Match Score</h2>
                <h1 style="color:white;">{score}%</h1>
            </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### ✅ Matched Keywords")
            if matched_keywords:
                st.success(", ".join(matched_keywords))
            else:
                st.warning("No strong keyword matches found.")

        with col2:
            st.markdown("### ❌ Missing Keywords (Add These)")
            if missing_keywords:
                st.error(", ".join(missing_keywords))
            else:
                st.success("No major keywords missing 🎉")
