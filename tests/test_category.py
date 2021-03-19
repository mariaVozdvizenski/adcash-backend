import requests
from models.category import Category
from schemas.category import CategorySchema, CategorySchemaPost

BASE_URL = "http://127.0.0.1:5000/categories/"
BASE_URL_ID = "http://127.0.0.1:5000/categories/{}/"

category_schema_post = CategorySchemaPost()
category_schema = CategorySchema()
category_schemas = CategorySchema(many=True)


def test_get_categories_returns_code_200():
    response = requests.get(BASE_URL)
    assert response.status_code == 200


def test_post_category_returns_code_200():
    category = Category(name="Electronics")
    response = requests.post(url=BASE_URL, json=category_schema_post.dump(category))
    assert response.status_code == 200


def test_post_category_returns_created_category():
    category = Category(name="Leisure")
    response = requests.post(url=BASE_URL, json=category_schema_post.dump(category))
    assert response.json()["name"] == category.name


def test_post_category_does_not_post_invalid_data():
    category = Category()
    response = requests.post(url=BASE_URL, json=category_schema_post.dump(category))
    assert response.status_code == 400


def test_get_nonexistent_category_returns_code_404():
    response = requests.get(BASE_URL_ID.format(999))
    assert response.status_code == 404


def test_get_category_returns_code_200():
    response = requests.get(BASE_URL_ID.format(1))
    assert response.status_code == 200


def test_get_category_returns_category_with_list_of_products():
    response = requests.get(BASE_URL_ID.format(1))
    assert response.json()["products"] is not None


def test_put_category_returns_code_200():
    get_response = requests.get(BASE_URL_ID.format(1))
    category = get_response.json()
    category["name"] = "Updated name"
    put_response = requests.put(url=BASE_URL_ID.format(1), json=category_schema_post.dump(category))
    assert put_response.json()["name"] == "Updated name"


def test_put_category_invalid_returns_code_400():
    updated_category = Category(id=2)
    put_response = requests.put(url=BASE_URL_ID.format(1), json=category_schema_post.dump(updated_category))
    assert put_response.status_code == 400


def test_delete_category_returns_code_200():
    category = Category(name="To Delete")
    post_response = requests.post(url=BASE_URL, json=category_schema_post.dump(category))
    category_id = post_response.json()["id"]
    delete_response = requests.delete(url=BASE_URL_ID.format(category_id))
    assert delete_response.status_code == 200


def test_delete_category_works():
    category = Category(name="To Delete")
    post_response = requests.post(url=BASE_URL, json=category_schema_post.dump(category))
    category_id = post_response.json()["id"]
    requests.delete(url=BASE_URL_ID.format(category_id))
    get_response = requests.get(url=BASE_URL_ID.format(category_id))
    assert get_response.status_code == 404

