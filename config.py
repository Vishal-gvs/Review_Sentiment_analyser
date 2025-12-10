"""
Configuration file for Flask application
"""
import os
from pathlib import Path

# Get the base directory
basedir = Path(__file__).parent.absolute()
instance_path = basedir / 'instance'
instance_path.mkdir(exist_ok=True)


def normalize_db_url(url: str) -> str:
    """
    Render PostgreSQL URLs sometimes start with 'postgres://'
    but SQLAlchemy requires 'postgresql://'
    """
    if url and url.startswith("postgres://"):
        return url.replace("postgres://", "postgresql://", 1)
    return url


class Config:
    """Base configuration"""

    # Secret key
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

    # Local SQLite path (fallback)
    database_path = instance_path / 'database.db'
    sqlite_uri = f"sqlite:///{database_path}"

    # Cloud database handling
    raw_db_url = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = normalize_db_url(raw_db_url) if raw_db_url else sqlite_uri

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Paths for ML model + vectorizer
    ML_MODEL_PATH = instance_path / 'sentiment_classifier.pkl'
    TFIDF_VECTORIZER_PATH = instance_path / 'tfidf_vectorizer.pkl'
