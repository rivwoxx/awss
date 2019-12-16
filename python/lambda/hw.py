#aws lambda hello-world example

import json

def lambda_handler(event, context):
    print("Hellow from lambda")
    return{
        'statusCode': 200,
        'body' : json.dumps('Hello from lambda!')
    }