import boto3

def handler(event,context):
    client = boto3.resource('dynamodb')
    table = client.Table('Products')
    response = table.put_item(
        Item={
            'product_id': event['product_id'],
            'product_name': event['product_name'],
            'product_category': event['product_category'],
            'product_description': event['product_description'],
            'product_cost': event['product_cost']
        }
    )

    return {
       'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
       'body': 'Record ' + event['product_id'] + ' added'
   }