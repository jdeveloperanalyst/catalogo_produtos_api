from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.controllers import product_controller

product_bp = Blueprint("products", __name__)

@product_bp.route("/", methods=["GET"])
def welcome():
    return jsonify("Bem vindo à API Catalogo de Produtos"), 200

@product_bp.route("/products", methods=["GET"])
@jwt_required()
def list_products():
    return jsonify(product_controller.list_products()[0]), 200


@product_bp.route("/products", methods=["POST"])
@jwt_required()
def create_product():
    data = request.get_json()
    identity = get_jwt_identity()
    claims = get_jwt()

    user = {
        "id": int(identity),
        "role": claims.get("role"),
        "username": claims.get("username"),
    }

    return product_controller.create_product(user, data)


@product_bp.route("/<int:product_id>", methods=["PUT"])
@jwt_required()
def update_product(product_id):
    data = request.get_json()
    identity = get_jwt_identity()
    claims = get_jwt()

    user = {
        "id": int(identity),
        "role": claims.get("role"),
        "username": claims.get("username"),
    }

    return product_controller.update_product(user, product_id, data)


@product_bp.route("/<int:product_id>", methods=["DELETE"])
@jwt_required()
def delete_product(product_id):
    identity = get_jwt_identity()
    claims = get_jwt()

    user = {
        "id": int(identity),
        "role": claims.get("role"),
        "username": claims.get("username"),
    }

    return product_controller.delete_product(user, product_id)
