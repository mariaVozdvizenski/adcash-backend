import requests
from models.product import Product
from schemas.product import ProductSchema, ProductSchemaPost, ProductSchemaPut

BASE_URL = "http://127.0.0.1:5000/products/"
BASE_URL_ID = "http://127.0.0.1:5000/products/{}/"

product_schema_post = ProductSchemaPost()
product_schema_put = ProductSchemaPut()

product_schema = ProductSchema()
product_schemas = ProductSchema(many=True)


def post_and_return_data(product):
    response = requests.post(url=BASE_URL, json=product_schema_post.dump(product))
    return product_schema.load(response.json())


def test_get_products_returns_code_200():
    response = requests.get(BASE_URL)
    assert response.status_code == 200


def test_post_product_returns_code_200():
    product = Product(name="Hobbit", price=10, category_id=1)
    response = requests.post(url=BASE_URL, json=product_schema_post.dump(product))
    assert response.status_code == 200


def test_post_product_returns_created_product():
    product = Product(name="Harry Potter", price=23.3, category_id=1)
    returned_data = post_and_return_data(product)
    assert returned_data.name == product.name


def test_post_product_does_not_let_post_invalid_data():
    product = Product(name="Harry Potter", price=23.3)
    response = requests.post(url=BASE_URL, json=product_schema_post.dump(product))
    assert response.status_code == 400


def test_post_product_url_works_without_trailing_slash():
    product = Product(name="Anna Karenina", price=14)
    response = requests.post(url="http://127.0.0.1:5000/products", json=product_schema_post.dump(product))
    assert response.status_code == 400


def test_get_product_returns_code_200():
    product_id = 1
    response = requests.get(BASE_URL_ID.format(product_id))
    assert response.status_code == 200


def test_get_nonexistent_product_returns_code_404():
    product_id = 99999
    response = requests.get(BASE_URL_ID.format(product_id))
    assert response.status_code == 404


def test_get_product_returns_correct_product():
    product = Product(name="Carrie", price=10, category_id=1)
    returned_product = post_and_return_data(product)
    response = requests.get(BASE_URL_ID.format(returned_product.id))
    assert product_schema.load(response.json()).id == returned_product.id


def test_delete_product_returns_status_code_200():
    product = Product(name="Jane Eyre", price=10.4, category_id=1)
    returned_product = post_and_return_data(product)
    response = requests.delete(BASE_URL_ID.format(returned_product.id))
    assert response.status_code == 200


def test_delete_product_deletes_the_product():
    product = Product(name="Runner", price=9, category_id=1)
    returned_product = post_and_return_data(product)
    requests.delete(BASE_URL_ID.format(returned_product.id))
    response = requests.get(BASE_URL_ID.format(returned_product.id))
    assert response.status_code == 404


def test_put_product_updates_data():
    product = Product(name="Some Book", price=10.45, category_id=1)
    returned_product = post_and_return_data(product)
    product_update = Product(name="Some Book Update", price=10, category_id=1, id=returned_product.id)
    response = requests.put(url=BASE_URL_ID.format(returned_product.id),
                            json=product_schema_put.dump(product_update))
    assert product_schema.load(response.json()).name == "Some Book Update"












