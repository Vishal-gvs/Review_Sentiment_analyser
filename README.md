Hotel Guest Sentiment Analyzer — NLP + Flask Web App

A full-stack machine-learning web application that analyzes hotel reviews, predicts sentiment, and stores user analysis history.
Built with Flask, NLTK, Scikit-Learn, TextBlob, PostgreSQL, and deployed on Render.

🔗 Live Demo: https://review-sentiment-analyser.onrender.com

(Free-tier Render instance may take 20–30 seconds to spin up)

📌 Overview

The Hotel Guest Sentiment Analyzer allows users to:

✓ Sign up, log in, and securely manage their account
✓ Enter single or multiple hotel reviews
✓ Perform NLP-based sentiment analysis
✓ View full polarity/subjectivity scores and model predictions
✓ Save analysis history in a database
✓ Explore a dashboard with past Review Sentiments
✓ Analyze a real dataset of 56 hotel reviews
✓ Visualize results using charts

This project combines Machine Learning, Natural Language Processing, and Full-Stack Web Development into one production-ready application.

🧠 Key Features
🔐 Authentication

User Signup / Login / Logout (Flask-Login)

Password hashing (secure)

📝 Sentiment Analysis

Rule-based polarity via TextBlob

ML-powered classifier with TF-IDF + Logistic Regression

Compound score computation

Support for:

Single review

Batch reviews

Real 56-review dataset

📊 Dashboard & Visualization

Shows user-specific history

Displays sentiment classifications and timestamps

Matplotlib & Seaborn charts

🗄 Database (PostgreSQL)

Stores users

Stores analysis results (review, sentiment, compound score, timestamp)

🌐 Deployment

Fully deployed on Render

Auto table creation on startup

Works with Render PostgreSQL

🧰 Tech Stack
Backend

Python 3

Flask

Flask-Login

Flask-SQLAlchemy

PostgreSQL (Render)

NLP / Machine Learning

NLTK

TextBlob

Scikit-Learn

TF-IDF Vectorizer

Logistic Regression Classifier

Frontend

HTML

CSS (custom styling)

Bootstrap 5

Jinja2 templates

Deployment

Render Web Service

Gunicorn

PostgreSQL Cloud Database

📂 Project Structure
Hotel_Guest_Analyser/
│
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── routes.py            # All routes & logic
│   ├── models.py            # SQLAlchemy models
│   ├── auth.py              # Authentication helpers
│   └── sentiment_analyzer.py # NLP + ML logic
│
├── templates/               # Frontend pages (HTML)
├── static/                  # CSS styles
│
├── instance/                # DB + ML model storage
│   ├── database.db          (local only)
│   ├── sentiment_classifier.pkl
│   └── tfidf_vectorizer.pkl
│
├── data/
│   └── hotel_reviews_dataset.csv
│
├── config.py                # Environment configs
├── run.py                   # App entrypoint for Gunicorn
├── requirements.txt         # Dependencies
└── README.md                # Documentation (this file)

⚙️ Installation (Local Setup)
1️⃣ Clone the repo
git clone https://github.com/Vishal-gvs/Review_Sentiment_analyser.git
cd Review_Sentiment_analyser

2️⃣ Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.\.venv\Scripts\activate    # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run app locally
python run.py


App runs at:

http://localhost:5000

🚀 Deployment (Render)
Required environment variables:
DATABASE_URL=<your render postgres internal/external URL>
SECRET_KEY=<your secret>

Optional environment variables:
AUTO_CREATE_DB=true   # set false to skip startup db.create_all()

Render Start Command:
gunicorn -w 4 -b 0.0.0.0:$PORT run:app


✔ Starts even if database is temporarily unreachable
✔ Auto-creates tables on startup (when AUTO_CREATE_DB=true)
✔ Works without Render Shell
✔ Fully cloud-ready

📊 Model Details
Preprocessing Steps:

Tokenization

Stopword removal

Lemmatization

TF-IDF vectorization

Classifier:

Logistic Regression (Scikit-Learn)

Trained using the included dataset

Outputs:

Positive

Negative

Neutral

Mixed

Compound score


🛠 Future Enhancements

REST API endpoint for sentiment prediction

JWT authentication

Real-time analysis dashboard

More advanced ML model (BERT, DistilBERT)

Docker containerization

Frontend redesign (React / Tailwind)
