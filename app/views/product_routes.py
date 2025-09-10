from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.product_controller import (
    list_products, create_product, update_product, delete_product
)

product_routes = Blueprint("product_routes", __name__)

@product_routes.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    return jsonify(*list_products())


@product_routes.route("/products", methods=["POST"])
@jwt_required()
def new_product():
    user = get_jwt_identity()
    return jsonify(*create_product(user, request.get_json()))


@product_routes.route("/products/<int:product_id>", methods=["PUT"])
@jwt_required()
def edit_product(product_id):
    user = get_jwt_identity()
    return jsonify(*update_product(user, product_id, request.get_json()))


@product_routes.route("/products/<int:product_id>", methods=["DELETE"])
@jwt_required()
def remove_product(product_id):
    user = get_jwt_identity()
    return jsonify(*delete_product(user, product_id))
