from flask import jsonify, request
from general import db
from models.product import Product
from schemas.product import ProductSchema, ProductSchemaPut
from helpers.errors import not_found, fk_invalid
from models.category import Category


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


def get_products():
    products = Product.query.all()

    return jsonify(products_schema.dump(products))


def get_product(product_id):
    product = Product.query.get(product_id)

    if product is None:
        return not_found, 404

    return jsonify(product_schema.dump(product))


def delete_product(product_id):
    product = Product.query.get(product_id)

    if product is None:
        return not_found, 404

    db.session.delete(product)
    db.session.commit()

    return product_schema.dump(product)


def put_product(product_id):
    products_schema_put = ProductSchemaPut()
    product_db = Product.query.get(product_id)

    if product_db is None:
        return not_found, 404

    data = request.get_json()
    print(data)
    errors = products_schema_put.validate(data)

    if errors:
        return errors, 400

    product = products_schema_put.load(data)

    if product.category_id is not None:
        category = Category.query.get(product.category_id)
        if category is None:
            return fk_invalid, 400
        else:
            product_db.category_id = product.category_id

    product_db.price = product.price
    product_db.name = product.name

    db.session.add(product_db)
    db.session.commit()

    return product_schema.dump(product_db)


def post_product():
    data = request.get_json()
    errors = product_schema.validate(data)

    if errors:
        return errors, 400

    product = product_schema.load(data)
    category = Category.query.get(product.category_id)

    if category is None:
        return fk_invalid, 400

    category.products.append(product)

    db.session.add(category)
    db.session.commit()

    return product_schema.dump(product)


