from flask import Flask
import logging
from app.extensions import db, migrate, jwt, bcrypt
from app.config import Config
from app.views.auth_routes import auth_routes
from app.views.user_routes import user_routes
from app.views.product_routes import product_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Registro das rotas
    app.register_blueprint(auth_routes, url_prefix="/auth")
    app.register_blueprint(user_routes, url_prefix="/users")
    app.register_blueprint(product_routes)

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
