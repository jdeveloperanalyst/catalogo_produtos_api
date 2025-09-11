from flask_jwt_extended import get_jwt_identity

def get_current_user():
    user = get_jwt_identity()
    return user, 200
