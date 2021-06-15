import os
import json

from shared_utils import send_response

from schema import ProductCreateSchema


# Always read environment variables from execution context.
PRODUCTS_TABLE_NAME = os.environ.get("PRODUCTS_TABLE_NAME")

# Define


def handler(event, context):

    request_body = json.loads(event["body"])

    # Validate request body
    product_create_schema = ProductCreateSchema()
    product_create_schema.load(request_body)

    # If not valid, raise an appropriate exception and return status 400.

    # Use send_response method to send response when a lambda is invoked from an API gateway.
    return send_response(status_code=200)