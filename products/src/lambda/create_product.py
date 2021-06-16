import os
import json
import boto3

from shared_utils import send_response, validate_schema, generate_uuid
from schema import CREATE_PRODUCT_REQUEST_SCHEMA
from jsonschema import validate

# Always read environment variables from execution context.
PRODUCTS_TABLE_NAME = os.environ.get("PRODUCTS_TABLE_NAME")

# Define


def handler(event, context):

    request_body = json.loads(event["body"])

    # Validate request body
    try:
        validate_schema(CREATE_PRODUCT_REQUEST_SCHEMA, request_body)
    # If not valid, raise an appropriate exception and return status 400.
    except Exception as e:
        return send_response(status_code=400, body={"message": e.message})

    # Generate UUID as product ID.
    product_id = generate_uuid()

    # Add product to dynamodb table.
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(PRODUCTS_TABLE_NAME)
    request_body["product_id"] = str(product_id)
    response = table.put_item(Item=request_body)

    # Things to consider: Product ID is hash key and category is sort key.
    # Please see if this will have any performance implications.
    # Think about what queries we will be running and choose keys appropriately.

    # Use send_response method to send response when a lambda is invoked from an API gateway.
    return send_response(status_code=200, body={"message": "product with id "+str(product_id)+" added"})