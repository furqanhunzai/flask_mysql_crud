from .database import db

class User(db.Model):
    __tablename__ = "users"                          # 1) table name in MySQL

    id = db.Column(db.Integer, primary_key=True)     # 2) integer primary key (auto-increment)
    name = db.Column(db.String(100), nullable=False) # 3) required text (max 100 chars)
    email = db.Column(db.String(120), unique=True, nullable=False)  # 4) must be unique + required

    def __repr__(self):
        return f"<User {self.name}>"
