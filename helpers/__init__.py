from general import db
from models.product import Product
from models.category import Category


def initialize_db():
    db.drop_all()
    db.create_all()
    book_1 = Product(price=6.5, name="Animal Farm")
    book_2 = Product(price=2.35, name="1984")
    category = Category(name="Literature")
    category.products.append(book_1)
    category.products.append(book_2)
    db.session.add(category)
    db.session.commit()
