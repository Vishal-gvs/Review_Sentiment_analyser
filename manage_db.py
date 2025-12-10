# manage_db.py
from app import create_app, db   # adjust import to your project structure

app = create_app()   # or from run import app if you expose it differently
with app.app_context():
    db.create_all()
    print("Database tables created")
