from flask import Flask
import logging
from app.extensions import db, jwt, bcrypt, migrate
from app.views.auth_routes import auth_bp
from app.views.user_routes import user_bp
from app.views.product_routes import product_bp
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Extensões
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Rotas
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(product_bp)

    # Configuração de log
    logging.basicConfig(level=logging.INFO)

    # Tratamento global de erros
    @app.errorhandler(Exception)
    def handle_global_exception(e):
        app.logger.error(f"Erro não tratado: {e}")
        return {"erro": "Erro interno no servidor"}, 500

    return app


app = create_app()
