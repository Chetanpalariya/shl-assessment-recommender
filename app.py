import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("shl_sample_assessments.csv")

# Fit TF-IDF on descriptions
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Description"])

# Recommend function
def recommend(query, top_n=10):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[::-1][:top_n]
    results = df.iloc[top_indices].copy()
    results["Similarity Score"] = similarities[top_indices]
    return results[[
        "Assessment Name", "URL", "Remote Testing Support", 
        "Adaptive/IRT Support", "Duration (mins)", 
        "Test Type", "Similarity Score"
    ]]

# Streamlit app
st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")

st.title("🔍 SHL Assessment Recommendation Engine")
st.write("Paste a job description or query below to get recommended assessments from SHL's catalog.")

user_query = st.text_area("Enter job description or hiring query:", height=200)

if st.button("Get Recommendations"):
    if user_query.strip() == "":
        st.warning("Please enter a query first.")
    else:
        results = recommend(user_query)
        st.success(f"Top {len(results)} recommendations found:")
        st.dataframe(results.reset_index(drop=True), use_container_width=True)
