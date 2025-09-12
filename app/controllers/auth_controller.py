from app.models.user import User
from app.extensions import db
from flask_jwt_extended import create_access_token


def register_user(username, password, role="user"):
    if User.query.filter_by(username=username).first():
        return {"error": "Usuário já existe"}, 400

    user = User(username=username, role=role)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return {"message": "Usuário registrado com sucesso"}, 201


def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return {"error": "Credenciais inválidas"}, 401

    # Aqui vai o ID como string no "sub" (identity) estudar esse trecho
    # e role/username como claims adicionais estudar esse trecho
    token = create_access_token(
        identity=str(user.id),
        additional_claims={
            "role": user.role,
            "username": user.username
        }
    )

    return {"access_token": token}, 200
