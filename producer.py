import time
import boto3
import random
import json
import uuid

client = boto3.client("kinesis", region_name = "us-west-2")
stream_name = 'kinesis-example'

jgls = ['Poppy', 'WuKong', 'Sejuani', 'LeeSin']
adcs = ['Twitch', 'Vayne', 'Ashe', 'Lucian']
mids = ['Diana', 'Fizz', 'Annie', 'Lux']
tops = ['Garen', 'Fiona', 'Irelia', 'Yasuo']
sups = ['Blizcrank', 'Leona', 'Lulu', 'Yuumi']

try:
    while True:
        data = {
            "id": str(uuid.uuid4()),
            'roster': {
                'top': random.choice(tops),
                'jgl': random.choice(jgls),
                'mid': random.choice(mids),
                'adc': random.choice(adcs),
                'sup': random.choice(sups)
            }
            
        }
        encoded_data = bytes(json.dumps(data).encode('utf-8'))
        print(f'sending: {data}')
        response = client.put_record(StreamName=stream_name, Data=encoded_data, PartitionKey=data['id'])
        print(f"sequence_number:{response['SequenceNumber']}")

        time.sleep(1)
except:
    print('error...')