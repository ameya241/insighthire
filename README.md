# 🚀 InsightHire AI  
### Resume vs Job Description Match Analyzer (AI Powered)

InsightHire AI is an intelligent resume analysis system that compares a candidate's resume with a job description and provides:

- 🎯 Match Score (Semantic Similarity)
- ✅ Matched Keywords
- ❌ Missing Keywords
- 📈 Improvement Insights

Built using **Streamlit + LangChain + Ollama + Embeddings**.

---

## 🧠 How It Works

InsightHire uses AI embeddings to:

1. Convert Resume into vector representation
2. Convert Job Description into vector representation
3. Compute cosine similarity score
4. Extract important keywords from Job Description
5. Compare keywords with Resume
6. Show missing skills to improve score

This ensures:
- Not just keyword matching
- But semantic (meaning-based) similarity scoring

---

## 🛠️ Tech Stack

- Python
- Streamlit (Frontend UI)
- Ollama (Local LLM & Embeddings)
- LangChain-Ollama
- Scikit-Learn (Cosine Similarity)
- PyPDF2 (PDF Parsing)
- NumPy

---

## 📂 Project Structure
insighthire/
│
<br>├── app.py # Streamlit frontend</br>
<br>├── rag_pipeline.py # Resume-JD scoring logic</br>
<br>├── README.md</br>
<br>└── testenv/ # Virtual environment</br>
