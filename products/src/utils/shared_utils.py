import uuid


def send_response(status_code, body=None):
    """
    A utility function to return a REST response from a lambda function.
    """
    return {
        "statusCode": status_code,
        "isBase64Encoded": "false",
        "headers": {"Content-Type": "application/json"},
        "body": body,
    }


def generate_uuid():
    return uuid.uuid4()
