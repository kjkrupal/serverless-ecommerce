import os
import json
import boto3
from boto3.dynamodb.conditions import Key

from schema import UPLOAD_PRODUCT_PHOTO_REQUEST_SCHEMA
from shared_utils import send_response, validate_schema

PHOTOS_BUCKET_NAME = os.environ.get("PHOTOS_BUCKET_NAME")
PRODUCTS_TABLE_NAME = os.environ.get("PRODUCTS_TABLE_NAME")


def handler(event, context):

    s3 = boto3.client("s3")

    request_body = json.loads(event["body"])
    product_id = event["pathParameters"]["product_id"]

    try:
        validate_schema(UPLOAD_PRODUCT_PHOTO_REQUEST_SCHEMA, request_body)
    except Exception as e:
        return send_response(status_code=400, body={"message": e.message})

    product_photo_key = product_id + "/" + request_body["file_name"]

    # Add photo folder name to dynamodb
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(PRODUCTS_TABLE_NAME)
    try:
        product = table.query(KeyConditionExpression=Key("product_id").eq(product_id))
    except Exception as e:
        return send_response(status_code=404, body={"message": e.message})

    print(product)

    product_photos = []
    if "Items" in product:
        if "product_photos" in product["Items"][0]:
            product_photos = product["Items"][0]["product_photos"]
        product_category = product["Items"][0]["product_category"]
    else:
        return send_response(status_code=404)

    print(product_photos)

    product_photos.append(product_photo_key)

    print(product_photos)

    table.update_item(
        Key={
            "product_id": product_id,
            "product_category": product_category,
        },
        UpdateExpression="set product_photos = :p",
        ExpressionAttributeValues={":p": product_photos},
    )

    url = s3.generate_presigned_url(
        ClientMethod="put_object",
        Params={
            "Bucket": PHOTOS_BUCKET_NAME,
            "Key": product_photo_key,
        },
        ExpiresIn=3600,
    )

    print(url)

    return send_response(status_code=200, body={"url": url})