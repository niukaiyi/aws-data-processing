import boto3
import concurrent.futures

def consume_shard(shard_id):

    shard_iterator = kinesis.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        ShardIteratorType=shard_iterator_type
    )['ShardIterator']

    while True:
        records = kinesis.get_records(ShardIterator=shard_iterator, Limit=10)
        for record in records['Records']:
            data = record['Data']
            print(f'read data from kinesis:{data}')

        shard_iterator = records['NextShardIterator']

if __name__ == "__main__":

    kinesis = boto3.client('kinesis', region_name='us-west-2')

    shard_iterator_type = 'TRIM_HORIZON'

    stream_name = 'kinesis-example'

    kinesis = boto3.client('kinesis', region_name='us-west-2')

    response = kinesis.describe_stream(StreamName=stream_name)
    shards = response['StreamDescription']['Shards']

    shard_ids = [shard['ShardId'].split('-')[1] for shard in shards]

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(shard_ids)) as executor:
        executor.map(consume_shard, shard_ids)

