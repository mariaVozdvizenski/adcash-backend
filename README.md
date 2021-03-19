# Adcash backend API
## Technical stack
* Python 3.8
* Flask
* Flask-SQLAlchemy
* Flask-Marshmallow
* Marshmallow
* SQLAlchemy
* Pytest

## Running the app 
Before proceeding make sure that you have pip installed
1. Navigate to <b>adcash-backend</b>
2. Install requirements
```console
pip install -r requirements.txt
```
Run main.py
```console
python main.py
```

## Running the tests
1. Open a new terminal (server has to be working)
2. Navigate to <b>adcash-backend/tests</b>
2. Run the following commands 

```console
python -m pytest test_product.py
python -m pytest test_category.py
```

## Endpoints

http://127.0.0.1:5000/products/ - Supports GET and POST
http://127.0.0.1:5000/categories/ - Supports GET and POST

http://127.0.0.1:5000/products/<id>/ - Supports GET, PUT and DELETE
http://127.0.0.1:5000/categories/<id>/ - Supports GET, PUT and DELETE

## Making requests
Below is shown how to make appropriate POST and PUT requests for each entity. Invalid requests are met with
an error message.

#### Category
POST, PUT  {name: "Some name"}

#### Product
POST, PUT {category_id: 2, name: "Some name", price: 3.4}
