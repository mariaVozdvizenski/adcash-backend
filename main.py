from general import app, db, ma
from helpers import initialize_db
import controllers.category
import controllers.product


@app.route('/')
def home():
    return "<h1>My API</h1>"


@app.route('/products/<int:product_id>/', methods=["PUT"])
def put_product(product_id):
    return controllers.product.put_product(product_id)


@app.route('/products/', methods=["POST"])
def post_product():
    return controllers.product.post_product()


@app.route('/products/<int:product_id>/', methods=["DELETE"])
def delete_product(product_id):
    return controllers.product.delete_product(product_id)


@app.route('/products/<int:product_id>/', methods=["GET"])
def get_product(product_id):
    return controllers.product.get_product(product_id)


@app.route('/products/')
def get_products():
    return controllers.product.get_products()


@app.route('/categories/')
def get_categories():
    return controllers.category.get_categories()


@app.route('/categories/<int:category_id>/', methods=["GET"])
def get_category(category_id):
    return controllers.category.get_category(category_id)


@app.route('/categories/', methods=["POST"])
def post_category():
    return controllers.category.post_category()


@app.route('/categories/<int:category_id>/', methods=["DELETE"])
def delete_category(category_id):
    return controllers.category.delete_category(category_id)


@app.route('/categories/<int:category_id>/', methods=["PUT"])
def put_category(category_id):
    return controllers.category.put_category(category_id)


if __name__ == "__main__":
    initialize_db()
    app.run(debug=True)
