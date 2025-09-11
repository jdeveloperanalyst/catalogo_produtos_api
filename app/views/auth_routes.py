from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import register_user, login_user


auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    return jsonify(*register_user(data.get("username"), data.get("password"), data.get("role", "user")))


@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return jsonify(*login_user(data.get("username"), data.get("password")))
