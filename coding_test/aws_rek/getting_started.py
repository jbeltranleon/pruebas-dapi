import boto3

s3 = boto3.resource('s3',
    aws_access_key_id='AKIAIUEYJCZTJUIVTIXA',
    aws_secret_access_key='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',
    region_name='us-east-1')

rekognition = boto3.client('rekognition',
    aws_access_key_id='AKIAIUEYJCZTJUIVTIXA',
    aws_secret_access_key='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',
    region_name='us-east-1')

print(s3.buckets.all())

for bucket in s3.buckets.all():
    print(bucket)
