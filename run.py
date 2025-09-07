from flask import Flask
from app.views.product_routes import routes
import logging

app = Flask(__name__)
app.register_blueprint(routes)

# Configura log básico
logging.basicConfig(level=logging.INFO)

# Captura exceções globais
@app.errorhandler(Exception)
def handle_global_exception(e):
    app.logger.error(f"Erro não tratado: {e}")
    return {"erro": "Erro interno no servidor"}, 500

if __name__ == "__main__":
    try:
        app.logger.info("Iniciando aplicação Flask...")
        app.run(host="0.0.0.0", port=54321, debug=True)
    except Exception as e:
        app.logger.critical(f"Falha ao iniciar o servidor: {e}")
