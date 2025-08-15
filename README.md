# AI-Powered-Job-Recommendation-System

## Overview

The **AI-Powered Job Recommendation System** is an intelligent application designed to help students, freshers, and job seekers discover the most relevant job and internship opportunities based on their unique skills, experience, and preferences. The system uses **Natural Language Processing (NLP)**, embeddings, and **Gemini LLM** to provide personalized job recommendations that align with the user’s profile.

Users can upload resumes in PDF format or manually input skills and preferences. The system then analyzes the data, computes similarity scores with a curated dataset of job postings, and returns the best matches along with detailed recommendation explanations.

This project demonstrates how AI can significantly improve the efficiency and effectiveness of job search by providing targeted, data-driven suggestions, reducing manual effort, and enhancing career decision-making for candidates.

---

## Industry Context

In today’s competitive job market, freshers and students often face difficulty in identifying job roles that match their skills and aspirations. Traditional job portals provide numerous listings, but most lack personalization and rely solely on keyword matching.

By leveraging AI, embeddings, and **Gemini LLM**, this system addresses these challenges:

* Offers **personalized job recommendations** rather than generic listings.
* Reduces time spent browsing irrelevant job postings.
* Helps candidates align their career choices with their skill sets and preferences.
* Provides an interactive, easy-to-use interface for seamless experience.

This approach represents the future of intelligent recruitment, where AI bridges the gap between candidates and job opportunities, making the process faster, more accurate, and user-centric.

---

## Features

* **Resume Parsing:** Extracts skills, experience, and education from uploaded PDF resumes using NLP techniques.
* **Manual Skill Input:** Allows users to enter their skills and preferences directly.
* **Job Matching:** Compares user profiles with job postings and calculates similarity using embeddings.
* **AI Recommendations:** Gemini LLM generates explanations and improves recommendation relevance.
* **Interactive Web Interface:** Built with Streamlit for easy navigation and results visualization.
* **Customizable Dataset:** Jobs are stored in JSON format, making it easy to add or update listings.
* **Similarity-Based Ranking:** Ranks jobs using cosine similarity or other vector similarity measures.

---

## Project Structure

```
app.py                 # Main Streamlit application
data/
  └── jobs.json         # Sample job postings dataset
src/
  ├── embed_utils.py    # Functions to generate embeddings
  ├── recommendation.py # Gemini LLM-based recommendation logic
  ├── utils.py          # Utility functions (e.g., load jobs)
requirements.txt        # Python dependencies
.env                    # Environment variables (API keys)
```

---

## Technologies Used

* **Python 3.8+** – Core programming language
* **Streamlit** – Web interface for uploading resumes and displaying recommendations
* **Gemini LLM** – AI-powered language model for personalized job recommendation explanations
* **LangChain** – Optional framework for managing embeddings and LLM chains
* **scikit-learn** – Similarity calculations for matching user profiles with jobs
* **PyPDF2** – Parsing resumes in PDF format
* **JSON/Database** – Job postings storage

---

## How It Works

1. **User Input:** The candidate uploads a resume (PDF) or enters skills manually.
2. **Text Extraction:** Resume text is parsed to identify skills, experience, and education.
3. **Embeddings Generation:** User input and job postings are converted into vector embeddings.
4. **Similarity Matching:** Cosine similarity (or other distance metrics) identifies the top-matching job postings.
5. **LLM Recommendations:** Gemini LLM optionally generates personalized explanations for recommended jobs.
6. **Results Display:** The Streamlit interface shows top jobs, their relevance scores, and detailed explanations.

This workflow ensures that candidates receive **high-quality, personalized recommendations** quickly and efficiently.

---

## Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/TejeswarReddy2000/AI-Powered-Job-Recommendation-System.git
cd AI-Powered-Job-Recommendation-System
```

2. **Create and activate a virtual environment**

```bash
python -m venv jobrec-env
# Windows
jobrec-env\Scripts\activate
# Mac/Linux
source jobrec-env/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Setup API keys**
   Create a `.env` file in the root directory and add:

```
GEMINIAPI_KEY=your_GEMINI_api_key_here
```

5. **Run the Streamlit app**

```bash
streamlit run app.py
```

6. **Access the application**
   Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Future Enhancements

* Integrate **live job scraping APIs** to update listings in real-time.
* Add **user authentication** and **profile saving** features.
* Expand job datasets with more industries, roles, and locations.
* Deploy on cloud platforms for public access.
* Enhance the **UI/UX** with advanced filters, sorting, and visualization options.
* Incorporate **multi-language support** for global users.
* Add **career path suggestions** and **salary predictions** using AI.

