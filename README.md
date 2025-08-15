# AI-Powered-Job-Recommendation-System

Overview
This project is an AI-powered job recommendation system designed to help students and job seekers find the most relevant job and internship opportunities based on their skills and preferences. The system leverages modern Natural Language Processing techniques including embeddings and Large Language Models (LLMs) for personalized recommendations. The app allows users to upload their resumes or manually enter skills, then matches them against a dataset of job postings.

Industry Context
In today’s competitive job market, students and freshers often struggle to find suitable job roles that match their unique skill sets and aspirations. Traditional job portals provide large volumes of listings but lack personalized recommendation capabilities. By integrating AI, embeddings, and retrieval-augmented generation, this system aims to simplify the job search process, reduce manual effort, and improve match quality.

Project Structure
├── app.py # Main Streamlit application

├── data/

│ └── jobs.json # Sample job postings dataset

├── src/

│ ├── embed_utils.py # Text embedding helper functions

│ ├── recommendation.py # LLM based recommendation logic

│ ├── utils.py # Utility functions (e.g., loading jobs)

│ └── groq_utils.py # Groq API integration (optional)

├── requirements.txt # Python dependencies

└── .env # Environment variables (API keys)

Steps to Run
Clone the repository:
git clone https://github.com/mounika2906/job-recommendation-system.git

cd job-recommendation-system
Create and activate a virtual environment:

python -m venv jobrec-env

Windows
jobrec-env\Scripts\activate

Mac/Linux
source jobrec-env/bin/activate

Install required packages:
pip install -r requirements.txt

Setup API keys:
Create a .env file in the root directory and add your API keys:

GROQ_API_KEY=your_groq_api_key_here

Run the Streamlit app:
streamlit run app.py

Open the app:
Visit http://localhost:8501 in your browser.

How It Works
Upload your resume (PDF) or manually enter your skills/preferences.

The app extracts key text from the resume or input.

It generates embeddings for the user input and all job postings.

Cosine similarity finds the top matching jobs from the dataset.

Optionally, an LLM (via Groq or OpenAI) generates personalized recommendation explanations.

Results are displayed in an interactive web UI built with Streamlit.

Technologies Used
Python 3.8+

Streamlit for the web interface

LangChain and Groq for embeddings and LLM-based recommendations

scikit-learn for similarity calculations

PyPDF2 for resume PDF parsing

### Future Enhancements
Integrate live job scraping APIs (Apify, Groq jobs)

Add user authentication and saved profiles

Expand datasets with more diverse job listings

Deploy the app on cloud services for public access

Improve UI with filters, sorting, and better design
