import os
import json
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
from shared_utils import send_response
from schema import GET_PRODUCT_REQUEST_SCHEMA
from jsonschema import validate

# Always read environment variables from execution context.
PRODUCTS_TABLE_NAME = os.environ.get("PRODUCTS_TABLE_NAME")

# Define


def handler(event, context):

    product_id = event["pathParameters"]["product_id"]
    # product_category = event["pathParameters"]["product_id"]

    # Add product to dynamodb table.
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(PRODUCTS_TABLE_NAME)
    try:
        response = table.query(KeyConditionExpression=Key('product_id').eq(product_id))
    except ClientError as e:
        return send_response(status_code=200, body={"message":e.response['Error']['Message']})

    print(response["Items"])
    # Things to consider: Product ID is hash key and category is sort key.
    # Please see if this will have any performance implications.
    # Think about what queries we will be running and choose keys appropriately.

    # Use send_response method to send response when a lambda is invoked from an API gateway.
    return send_response(status_code=200, body={"Item": response["Items"]})