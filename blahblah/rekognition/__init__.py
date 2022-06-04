import boto3

from blahblah.config import Config

rekognition = boto3.client("rekognition",
                           aws_access_key_id=Config.ACCESS_KEY,
                           aws_secret_access_key=Config.SECRET_KEY,
                           region_name="ap-northeast-2")

ingredient_list={'Onion':'양파','Potato':'감자','Broccoli':'브로콜리',
                'Sweet potato':'고구마','Leek':'파',',Egg':'계란',
                'Mushroom':'버섯', 'Amanita':'버섯', 'Squash':'호박',
                'Pumpkin':'호박', "Pork":'고기',"Ham":"햄","Noodle":'면',
                'Pasta':'면','Spaghetti':'면', 'Carrot':'당근', 
                'Bean Sprout':'숙주'}