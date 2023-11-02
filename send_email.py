import json
import boto3


client = boto3.client('ses', region_name='us-west-2')
sender = ''
receiver = ''
subject = 'test-email'

def lambda_handler(event, context):
    client.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [
                receiver,
            ]
        },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': 'This is a test email',
                    'Charset': 'UTF-8'
                }
            }
        }
    )