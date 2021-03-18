from general import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    products = db.relationship("Product",
                               lazy=False,
                               backref=db.backref("category", lazy=False)
                               )

    def __repr__(self):
        return '<Category %r>' % self.name
