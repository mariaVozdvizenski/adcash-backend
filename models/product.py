from general import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer,
                            db.ForeignKey('category.id'),
                            nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.name

