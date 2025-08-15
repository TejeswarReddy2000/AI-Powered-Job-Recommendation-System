import streamlit as st
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# --------------------------
# Load embedding model
# --------------------------
embedder = SentenceTransformer("paraphrase-MiniLM-L3-v2", device="cpu")

# --------------------------
# Preloaded sample jobs
# --------------------------
jobs = [
    {"title": "Data Analyst", "companyName": "ABC Tech", "location": "Hyderabad, India",
     "experienceLevel": "Entry", "workType": "Full-time",
     "description": "Analyze datasets and generate insights using Python, SQL, Excel.",
     "jobUrl": "https://example.com/job/1"},
    {"title": "Data Analyst", "companyName": "XYZ Solutions", "location": "Bangalore, India",
     "experienceLevel": "Mid", "workType": "Full-time",
     "description": "Create dashboards and reports using Python and SQL.",
     "jobUrl": "https://example.com/job/2"},
    # Repeat or generate more jobs
]

# You can duplicate or generate more sample jobs here to reach 50
for i in range(3, 51):
    jobs.append({
        "title": "Data Analyst",
        "companyName": f"Company {i}",
        "location": "India",
        "experienceLevel": "Entry",
        "workType": "Full-time",
        "description": "Analyze datasets and generate insights using Python, SQL, Excel.",
        "jobUrl": f"https://example.com/job/{i}"
    })

# --------------------------
# Extract text from PDFs
# --------------------------
def get_pdf_text(pdf_doc):
    text = ""
    try:
        pdf_reader = PdfReader(pdf_doc)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    except Exception as e:
        st.error(f"Error reading {pdf_doc.name}: {e}")
    return text

# --------------------------
# Split text into chunks
# --------------------------
def split_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks

# --------------------------
# Create FAISS vector store
# --------------------------
def create_vector_store(chunks):
    if not chunks:
        return None, []
    first_emb = embedder.encode([chunks[0]]).astype('float32')
    dim = first_emb.shape[1]
    index = faiss.IndexFlatL2(dim)
    embeddings = np.array(embedder.encode(chunks)).astype('float32')
    index.add(embeddings)
    return index, chunks

# --------------------------
# Search similar chunks
# --------------------------
def search_chunks(index, chunks, query, top_k=3):
    if index is None:
        return []
    query_emb = np.array(embedder.encode([query])).astype('float32')
    D, I = index.search(query_emb, top_k)
    return [chunks[i] for i in I[0]]

# --------------------------
# Recommend jobs based on skills
# --------------------------
def recommend_jobs(jobs, skills):
    recommended = []
    for job in jobs:
        title = job.get("title", "")
        desc = job.get("description", "")
        if any(skill.lower() in title.lower() or skill.lower() in desc.lower() for skill in skills):
            recommended.append(job)
    return recommended

# --------------------------
# Streamlit App
# --------------------------
def main():
    st.set_page_config(page_title="Resume Job Matcher")
    st.title("AI-Powered Job Recommendation System")

    if 'index' not in st.session_state:
        st.session_state.index = None
        st.session_state.chunks = None
        st.session_state.raw_text = ""

    # Upload PDF
    pdf_doc = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    if st.button("Process Resume") and pdf_doc:
        with st.spinner("Processing Resume..."):
            raw_text = get_pdf_text(pdf_doc)
            chunks = split_text(raw_text)
            index, chunk_list = create_vector_store(chunks)
            st.session_state.index = index
            st.session_state.chunks = chunk_list
            st.session_state.raw_text = raw_text
            st.success("Resume processed! You can now ask questions or see job matches.")

    # Ask a question
    user_question = st.text_input("Ask a question about your Resume:")
    if user_question and st.session_state.raw_text:
        top_chunks = search_chunks(st.session_state.index, st.session_state.chunks, user_question)
        context = "\n".join(top_chunks)
        answer = context if context else "The answer is not available in the uploaded resume."
        st.markdown(f"**Answer:** {answer}")

    # Recommend jobs automatically based on skills extracted
    if st.session_state.raw_text:
        st.subheader("Recommended Jobs Based on Resume Skills")
        # Simple keyword extraction (skills in resume)
        skills = ["python", "sql", "excel", "tableau", "power bi"]  # Add more if needed
        # Filter only the skills present in resume
        skills_in_resume = [skill for skill in skills if skill.lower() in st.session_state.raw_text.lower()]
        recommended = recommend_jobs(jobs, skills_in_resume)
        if recommended:
            for job in recommended:
                st.markdown(f"**{job.get('title','')}** at *{job.get('companyName','')}*")
                st.markdown(f"Location: {job.get('location','')}")
                st.markdown(f"Experience: {job.get('experienceLevel','')}")
                st.markdown(f"Work Type: {job.get('workType','')}")
                st.markdown(f"[Job Link]({job.get('jobUrl','')})")
                st.markdown("---")
        else:
            st.info("No recommended jobs found based on your resume.")

if __name__ == "__main__":
    main()
