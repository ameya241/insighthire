from langchain_ollama import OllamaEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re


def analyze_resume_vs_jd(resume_text, jd_text):

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # Generate embeddings
    resume_vector = embeddings.embed_query(resume_text)
    jd_vector = embeddings.embed_query(jd_text)

    resume_vector = np.array(resume_vector).reshape(1, -1)
    jd_vector = np.array(jd_vector).reshape(1, -1)

    # Cosine similarity score
    similarity = cosine_similarity(resume_vector, jd_vector)[0][0]
    score = round(similarity * 100, 2)

    # Keyword Matching
    jd_words = set(re.findall(r'\b[A-Za-z]+\b', jd_text.lower()))
    resume_words = set(re.findall(r'\b[A-Za-z]+\b', resume_text.lower()))

    stopwords = {
        "and", "or", "the", "a", "an", "to", "of",
        "in", "with", "for", "on", "at", "by", "is",
        "are", "this", "that", "from"
    }

    jd_keywords = {word for word in jd_words if len(word) > 3 and word not in stopwords}

    missing_keywords = list(jd_keywords - resume_words)
    matched_keywords = list(jd_keywords & resume_words)

    return score, missing_keywords[:20], matched_keywords[:20]
