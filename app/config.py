import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

class Config:
    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "changeme")

    # JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "changemejwt")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 300))  # segundos

    # Banco de dados
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False").lower() in ("true", "1")

    # App
    APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT = int(os.getenv("APP_PORT", 5000))
    TZ = os.getenv("TZ", "UTC")
