CREATE_PRODUCT_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "productName": {"description": "Name of the product", "type": "string"},
        "productCategory": {
            "description": "The Category of the product",
            "type": "string",
        },
        "productDescription": {"description": "Desc of the product", "type": "string"},
        "productPrice": {"description": "Price of the product", "type": "number"},
        "productPriceCurrency": {
            "description": "Currency of the product",
            "type": "string",
        },
        "productAttributes": {
            "description": "Attributes of the product",
            "type": "object",
        },
    },
    "required": [
        "productName",
        "productPrice",
        "productDescription",
        "productCategory",
        "productPriceCurrency",
        "productAttributes",
    ],
}
