CREATE_PRODUCT_REQUEST_SCHEMA = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ecommerce.com/create_product.schema.json",
  "title": "Create Product",
  "description": "Create product lambda",
  "type": "object",
  "properties": {
    "productName": {
      "description": "Name of the product",
      "type": "string"
    },
    "productCategory": {
      "description": "The Category of the product",
      "type": "string",
      "exclusiveMinimum": 0
    },
    "productDescription":{
      "description": "Desc of the product",
      "type": "string"
    },
    "productPrice":{
      "description": "Price of the product",
      "type": "number"
    },
    "productPriceCurrency": {
      "description": "Currency of the product",
      "type": "string"
    },
    "productAttributes": {
      "description": "Attributes of the product",
      "type": "object"
    }
  },
  "required": ["productName", "productPrice", "productDescription", "productCategory", "productPriceCurrency", "productAttributes"]
}















#from marshmallow import Schema, fields



# class ProductCreateSchema(Schema):
#     product_category = fields.Str(required=True)
#     product_name = fields.Str(required=True)
#     product_description = fields.Str(required=True)
#     product_price = fields.Number(required=True)
#     product_price_currency = fields.Str(required=True)
#     product_attributes = fields.Dict(
#         keys=fields.Str(), values=fields.Str(), required=False
#     )
