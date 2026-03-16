import os
import json
import boto3
sns = boto3.client('sns')
TOPIC_ARN = os.environ['TOPIC_ARN']
def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        message = f"New file uploaded: s3://{bucket}/{key}"
        sns.publish(TopicArn=TOPIC_ARN, Message=message, Subject="New Report Uploaded")
    return {'statusCode': 200, 'body': json.dumps('Notification sent')}
