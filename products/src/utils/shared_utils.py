import jsonschema
import uuid
import json

from decimal import Decimal


class ProductsEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, Decimal):
            return float(obj)

        return json.JSONEncoder.default(self, obj)


def send_response(status_code, body=None):
    """
    A utility function to return a REST response from a lambda function.
    """
    return {
        "statusCode": status_code,
        "isBase64Encoded": "false",
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body, cls=ProductsEncoder) if body else None,
    }


def generate_uuid():
    return uuid.uuid4()


def validate_schema(schema, instance):
    try:
        jsonschema.validate(instance=instance, schema=schema)
    except Exception as e:
        raise e