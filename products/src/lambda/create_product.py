import os

from shared_utils import send_response


# Always read environment variables from execution context.
PRODUCTS_TABLE_NAME = os.environ.get("PRODUCTS_TABLE_NAME")


def handler(event, context):

    print(event)

    print(context)

    print(PRODUCTS_TABLE_NAME)

    # Use send_response method to send response when a lambda is invoked from an API gateway.
    return send_response(status_code=200)