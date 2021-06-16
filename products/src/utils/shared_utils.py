import jsonschema
import uuid
import json


def send_response(status_code, body=None):
    """
    A utility function to return a REST response from a lambda function.
    """
    return {
        "statusCode": status_code,
        "isBase64Encoded": "false",
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body) if body else None,
    }


def generate_uuid():
    return uuid.uuid4()


def validate_schema(schema, instance):
    try:
        jsonschema.validate(instance=instance, schema=schema)
    except Exception as e:
        raise e