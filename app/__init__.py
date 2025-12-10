"""
Flask application factory
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Initialize extensions
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'routes.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    """Application factory function"""

    # Resolve absolute paths for templates and static files
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(root_dir, 'templates')
    static_dir = os.path.join(root_dir, 'static')

    # Create Flask application instance
    app = Flask(
        __name__,
        template_folder=template_dir,
        static_folder=static_dir
    )

    # Load configuration (works for Render + local)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Flask-Login user loader
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    # Import and register blueprints
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    # -------------------------------
    # AUTO-CREATE DATABASE TABLES
    # (Required because free Render plan
    #  does NOT allow Shell or migrations)
    # -------------------------------
    with app.app_context():
        db.create_all()
        print("✓ Database tables ensured (Render-friendly auto-create).")

    return app
