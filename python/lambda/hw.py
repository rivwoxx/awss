#aws lambda hello-world example

import json
# import boto3

def lambda_handler(event, context):
    print("Hellow from lambda")
    return{
        'statusCode': 200,
        'body' : json.dumps('Hello from lambda!')
    }

    # # Create an SNS client
    # sns = boto3.client('sns')

    # # Publish a simple message to the specified SNS topic   
    # response = sns.publish(
    #     TopicArn='arn:aws:sns:region:0123456789:my-topic-arn',    
    #     Message='Hello World!',    
    # )

    # # Print out the response
    # print(response)