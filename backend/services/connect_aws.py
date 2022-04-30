import boto3

from backend.services.aws_keys import ACCESS_KEY_ID, ACCESS_SECRET_KEY

s3 = boto3.client('s3',
                  aws_access_key_id=ACCESS_KEY_ID,
                  aws_secret_access_key=ACCESS_SECRET_KEY)

BUCKET_NAME = 'onlinestore-media-images'
