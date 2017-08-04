import tweepy
import time
import os.path
import sys
sys.path.append(os.path.dirname(__file__))
import train
#di=os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
#from haikubot import train
from os.path import join, dirname
from dotenv import load_dotenv,find_dotenv

#commented code below is used to run bot locally
dir=os.path.dirname(os.path.dirname(__file__))
dotenv_path = join(dir, '.env')
load_dotenv(dotenv_path)
load_dotenv(find_dotenv())

auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
auth.set_access_token(os.environ['access_token'],os.environ['access_token_secret'])
#auth.set_access_token(S3Connection(os.environ['access_token'], os.environ['access_token_secret']))

api = tweepy.API(auth)

trainOb=train.train()
textModel=trainOb.trainOnFiles()

while True:
    haiku=trainOb.genHaiku(textModel)
    api.update_status(haiku)
    time.sleep(24*60*60)