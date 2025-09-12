from app.models.product import Product
from app.extensions import db

def list_products():
    products = Product.query.all()
    return [
        {"id": p.id, "name": p.name, "description": p.description, "owner": p.creator.username}
        for p in products
    ], 200


def create_product(user, data):
    product = Product(
        name=data["name"],
        description=data.get("description"),
        created_by=user["id"]
    )
    db.session.add(product)
    db.session.commit()
    return {"message": "Produto criado com sucesso"}, 201


def update_product(user, product_id, data):
    product = Product.query.get_or_404(product_id)

    if user["role"] != "admin" and product.created_by != user["id"]:
        return {"error": "Você não tem permissão para editar este produto"}, 403

    product.name = data.get("name", product.name)
    product.description = data.get("description", product.description)
    db.session.commit()
    return {"message": "Produto atualizado com sucesso"}, 200


def delete_product(user, product_id):
    product = Product.query.get_or_404(product_id)

    if user["role"] != "admin" and product.created_by != user["id"]:
        return {"error": "Você não tem permissão para excluir este produto"}, 403

    db.session.delete(product)
    db.session.commit()
    return {"message": "Produto deletado com sucesso"}, 200
