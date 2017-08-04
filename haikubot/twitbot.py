import tweepy
import time
from haikubot import credentials, train
import os


#s3=boto.connect_s3()

#auth=tweepy.OAuthHandler(con_key,con_sec)
#acc_token=os.environ.get('access_token',True)
#acc_token_secret=os.environ.get('access_token_secret',True)
#auth.set_access_token(acc_token,acc_token_secret)


#s3=S3Connection(os.environ['consumer_key'], os.environ['consumer_secret'])
#auth=tweepy.OAuthHandler(s3)
#conn2=S3Connection(os.environ['access_token'], os.environ['access_token_secret'])

#bucket = conn1.create_bucket('botbucket')

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