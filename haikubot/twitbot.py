import tweepy
from time import sleep
from haikubot import credentials, train


auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)


trainOb=train.train()
textModel=trainOb.trainOnFiles()


haiku=trainOb.genHaiku(textModel)
api.update_status(haiku)