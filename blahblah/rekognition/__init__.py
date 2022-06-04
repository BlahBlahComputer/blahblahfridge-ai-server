import boto3

from blahblah.config import Config

rekognition = boto3.client("rekognition",
                           aws_access_key_id=Config.ACCESS_KEY,
                           aws_secret_access_key=Config.SECRET_KEY,
                           region_name="ap-northeast-2")