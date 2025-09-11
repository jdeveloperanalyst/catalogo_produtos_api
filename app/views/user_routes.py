from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.controllers.user_controller import get_current_user

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/me", methods=["GET"])
@jwt_required()
def me():
    return jsonify(*get_current_user())
