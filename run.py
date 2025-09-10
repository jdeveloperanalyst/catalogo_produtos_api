from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
import logging

from app.config import Config
from app.views.auth_routes import auth_bp
from app.views.user_routes import user_bp
from app.views.product_routes import product_bp

# Inicialização das extensões
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Registro das rotas
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(product_bp, url_prefix="/products")

    # Configuração de log
    logging.basicConfig(level=logging.INFO)

    # Tratamento global de erros
    @app.errorhandler(Exception)
    def handle_global_exception(e):
        app.logger.error(f"Erro não tratado: {e}")
        return {"erro": "Erro interno no servidor"}, 500

    return app


# Entry point
if __name__ == "__main__":
    app = create_app()
    try:
        app.logger.info("Iniciando aplicação Flask...")
        app.run(host=Config.APP_HOST, port=Config.APP_PORT, debug=True)
    except Exception as e:
        app.logger.critical(f"Falha ao iniciar o servidor: {e}")
