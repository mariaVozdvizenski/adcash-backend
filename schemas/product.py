from marshmallow.validate import Length
from general import ma
from models.product import Product
from marshmallow import fields, post_load


class ProductSchemaPost(ma.SQLAlchemySchema):
    class Meta:
        model = Product

    name = fields.Str(required=True, validate=Length(min=1, max=255))
    price = ma.auto_field()
    category_id = ma.auto_field()

    @post_load
    def create_product(self, data, **kwargs):
        return Product(**data)


class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product

    id = ma.auto_field()
    name = fields.Str(required=True, validate=Length(min=1, max=255))
    price = ma.auto_field()
    category_id = ma.auto_field()

    @post_load
    def create_product(self, data, **kwargs):
        return Product(**data)


class ProductSchemaPut(ma.SQLAlchemySchema):
    class Meta:
        model = Product

    id = ma.auto_field()
    name = fields.Str(validate=Length(min=1, max=255))
    price = fields.Decimal()
    category_id = fields.Integer()

    @post_load
    def create_product(self, data, **kwargs):
        return Product(**data)
