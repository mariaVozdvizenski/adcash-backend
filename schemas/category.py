from marshmallow.validate import Length
from general import ma
from models.category import Category
from marshmallow import fields, post_load
from .product import ProductSchema


class CategorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Category

    id = ma.auto_field()
    name = fields.Str(required=True, validate=Length(min=1, max=255))
    products = fields.Nested(ProductSchema(only=("id", "name")), many=True)

    @post_load
    def create_category(self, data, **kwargs):
        return Category(**data)


