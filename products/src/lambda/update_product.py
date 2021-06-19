import os
import json
import boto3

from shared_utils import send_response, validate_schema, generate_uuid
from schema import UPDATE_PRODUCT_REQUEST_SCHEMA
from jsonschema import validate
from boto3.dynamodb.conditions import Key
from decimal import Decimal

# Always read environment variables from execution context.
PRODUCTS_TABLE_NAME = os.environ.get("PRODUCTS_TABLE_NAME")

# Define


def handler(event, context):

    request_body = json.loads(event["body"])
    product_id = event["pathParameters"]["product_id"]
    # Validate request body
    try:
        validate_schema(UPDATE_PRODUCT_REQUEST_SCHEMA, request_body)
    # If not valid, raise an appropriate exception and return status 400.
    except Exception as e:
        return send_response(status_code=400, body={"message": e.message})

    # Add product to dynamodb table.
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(PRODUCTS_TABLE_NAME)
    

    product = table.query(
        KeyConditionExpression=Key('product_id').eq(product_id)
    )

    if "Items" in product:
        product_category = product["Items"][0]["product_category"]
    
    response = table.update_item(
            Key={
                'product_id': product_id,
                'product_category': product_category
            },
            UpdateExpression = "set product_name=:a, product_price=:b, product_description=:c, product_category=:d, product_price_currency=:e, product_attributes=:f",
            ExpressionAttributeNames={
                ':a': request_body["product_name"],
                ':b': Decimal(request_body["product_price"]),
                ':c': request_body["product_description"],
                ':d': request_body["product_category"],
                ':e': request_body["product_price_currency"],
                ':f': request_body["product_attributes"]
            },
            ReturnValues="UPDATED_NEW"
        )

    # Things to consider: Product ID is hash key and category is sort key.
    # Please see if this will have any performance implications.
    # Think about what queries we will be running and choose keys appropriately.

    # Use send_response method to send response when a lambda is invoked from an API gateway.
    return send_response(status_code=200, body={"message": "product with id "+str(product_id)+" added"})