import csv
import tweepy
import os
import json
from pull_new_followers import updateFollowing
from since_post import check_last_retweet
from bot import readCSV,writeCSV,retweet_latest



def Authenticate(file_name):
  with open(file_name) as f:
    params=json.load(f)
  auth = tweepy.OAuthHandler(params["consumer_key"], params["consumer_secret"])
  auth.set_access_token(params['access_token'], params["access_token_secret"])
  return tweepy.API(auth)



api=Authenticate('./keys.json')
if os.path.isfile('dict.csv'):
  pass
else:
  os.mkdir('dict.csv')
updateFollowing("dict.csv")
check_last_retweet('dict.csv')
retweet_latest('dict.csv')


