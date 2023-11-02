import boto3
import uuid
import random

jgls = ['Poppy', 'WuKong', 'Sejuani', 'LeeSin']
adcs = ['Twitch', 'Vayne', 'Ashe', 'Lucian']
mids = ['Diana', 'Fizz', 'Annie', 'Lux']
tops = ['Garen', 'Fiona', 'Irelia', 'Yasuo']
sups = ['Blizcrank', 'Leona', 'Lulu', 'Yuumi']

names = jgls + adcs + mids + tops + sups
table_name = 'Student'

dynamodb = boto3.client('dynamodb', region_name='us-west-2')




for i in range(0, 3):
    data = {
        'Id': {'S': str(uuid.uuid4())},
        'Name': {'S': random.choice(names)}
    }
    response = dynamodb.put_item(
        TableName=table_name,
        Item=data
    )
    print(response)

    


