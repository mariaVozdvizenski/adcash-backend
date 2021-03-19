from flask import jsonify, request
from general import db
from models.category import Category
from schemas.category import CategorySchema, CategorySchemaPost
from helpers.errors import not_found

category_schema_post = CategorySchemaPost()
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


def get_categories():
    categories = Category.query.all()
    return jsonify(categories_schema.dump(categories))


def get_category(category_id):
    category = Category.query.get(category_id)

    if category is None:
        return not_found, 404

    return category_schema.dump(category)


def post_category():
    data = request.get_json()
    errors = category_schema_post.validate(data)

    if errors:
        return errors, 400

    category = category_schema_post.load(data)
    db.session.add(category)
    db.session.commit()

    return category_schema.dump(category)


def put_category(category_id):
    category_db = Category.query.get(category_id)

    if category_db is None:
        return not_found, 404

    data = request.get_json()
    errors = category_schema_post.validate(data)

    if errors:
        return errors, 400

    category = category_schema_post.load(data)
    category_db.name = category.name

    db.session.add(category_db)
    db.session.commit()

    return category_schema.dump(category_db)


def delete_category(category_id):
    category_db = Category.query.get(category_id)

    if category_db is None:
        return not_found, 404

    db.session.delete(category_db)
    db.session.commit()

    return category_schema.dump(category_db)


