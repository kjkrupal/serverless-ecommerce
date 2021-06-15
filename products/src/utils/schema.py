from marshmallow import Schema, fields


class ProductCreateSchema(Schema):
    product_category = fields.Str(required=True)
    product_name = fields.Str(required=True)
    product_description = fields.Str(required=True)
    product_price = fields.Number(required=True)
    product_price_currency = fields.Str(required=True)
    product_attributes = fields.Dict(
        keys=fields.Str(), values=fields.Str(), required=False
    )
