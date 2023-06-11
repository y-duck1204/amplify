import json
import boto3

from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('anplify-test-table')

now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
print(now)


def lambda_handler(event, context):
    # TODO implement
    name = event['firstName'] + ' ' + event['lastName']
    
    response = table.put_item(
        Item={
            'ID': name,
            'LatestGreetingTime': now
        })
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! ' + name)
    }