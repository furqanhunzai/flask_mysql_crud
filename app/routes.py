from flask import Blueprint, request, jsonify
from .database import db
from .models import User
from sqlalchemy.exc import IntegrityError


main = Blueprint("main", __name__)

# CREATE
@main.route("/users", methods=["POST"])
def create_user():
  
    data = request.get_json()
    print("data",data)
    new_user = User(name=data["name"], email=data["email"])

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully"}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists"}), 400




# READ ALL
@main.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    result = [{"id": u.id, "name": u.name, "email": u.email} for u in users]
    return jsonify(result)


# READ ONE
@main.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email})


# UPDATE
@main.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    db.session.commit()
    return jsonify({"message": "User updated successfully"})


# DELETE
@main.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})
