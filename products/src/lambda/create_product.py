import os
import json

from shared_utils import send_response, validate_schema
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
    except Exception as e:
        print(e)
        print(e.__dict__)
        return send_response(status_code=400)
    # If not valid, raise an appropriate exception and return status 400.

    # Use send_response method to send response when a lambda is invoked from an API gateway.
    return send_response(status_code=200)