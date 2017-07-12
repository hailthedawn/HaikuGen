import tweepy
import time
from haikubot import train
import os


auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
auth.set_access_token(os.environ['access_token'], os.environ['access_token_secret'])
api = tweepy.API(auth)


trainOb=train.train()
textModel=trainOb.trainOnFiles()

while True:
    haiku=trainOb.genHaiku(textModel)
    api.update_status(haiku)
    time.sleep(24*60*60)