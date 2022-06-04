import boto3

from blahblah.config import Config

s3 = boto3.client("s3",
                    aws_access_key_id=Config.ACCESS_KEY,
                    aws_secret_access_key=Config.SECRET_KEY,
                    region_name="ap-northeast-2")