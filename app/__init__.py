from flask import Flask
from .database import db, init_db
from .routes import main
from .config import Config

def create_app():
    app = Flask(__name__)                  # 1️⃣ Create Flask app object
    app.config.from_object(Config)         # 2️⃣ Load config (like DB URL)

    db.init_app(app)                       # 3️⃣ Connect Flask app to database
    with app.app_context():                # 4️⃣ Activate app context
        init_db()                          # 5️⃣ Create tables in MySQL

    app.register_blueprint(main)           # 6️⃣ Add routes (API endpoints)
    return app                             # 7️⃣ Return final app
