from flask import Blueprint, Response
import json

routes = Blueprint("product_routes", __name__)

@routes.route("/")
def home():
    try:
        return "<h1>Página Inicial</h1>", 200
    except Exception as e:
        routes.logger.error(f"Erro na rota '/': {e}")
        return json(Response({"erro": "Falha ao carregar a página"})), 500

