CREATE_PRODUCT_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "product_name": {"description": "Name of the product", "type": "string"},
        "product_category": {
            "description": "The Category of the product",
            "type": "string",
        },
        "product_description": {"description": "Desc of the product", "type": "string"},
        "product_price": {"description": "Price of the product", "type": "number"},
        "product_price_currency": {
            "description": "Currency of the product",
            "type": "string",
        },
        "product_attributes": {
            "description": "Attributes of the product",
            "type": "object",
        },
    },
    "required": [
        "product_name",
        "product_price",
        "product_description",
        "product_category",
        "product_price_currency",
        "product_attributes",
    ],
}

UPLOAD_PRODUCT_PHOTO_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "file_name": {"description": "Name of the photo file", "type": "string"}
    },
    "required": [
        "file_name",
    ],
}