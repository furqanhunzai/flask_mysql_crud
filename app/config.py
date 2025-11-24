import os
from dotenv import load_dotenv

load_dotenv()  # 1) read .env file into OS environment

class Config:
    # 2) pull DATABASE_URL from environment (set in .env)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    # 3) turn off a noisy SQLAlchemy change-tracking feature we don’t need
    SQLALCHEMY_TRACK_MODIFICATIONS = False
