from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 1) global SQLAlchemy object we’ll use everywhere

def init_db():
    from .models import User  # 2) import models inside to avoid circular imports
    db.create_all()           # 3) create tables if they don’t exist (uses connected DB)
