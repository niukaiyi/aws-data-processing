import json
import base64
import boto3

def lambda_handler(event, context):
    records = event['Records']
    for record in records:
        encoded_data = record['kinesis']['data']
        decoded_data = base64.b64decode(encoded_data)
        sequence_number = record['kinesis']['sequenceNumber']
        send_to_s3(decoded_data, sequence_number)
   
s3 = boto3.client('s3')   
bucket = 'kaiyi-us-east-2-bucket-training-day-2-02'

def send_to_s3(data, sequenceNumber):
    file_name = f'{sequenceNumber}.json'
    s3_path = 'kinesis_data/' + file_name
    response = s3.put_object(Bucket=bucket, Key=s3_path, Body=data)