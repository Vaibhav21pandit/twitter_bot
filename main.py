import csv
import os
os.system('pip install tweepy')
import tweepy
import json
from since_post import check_last_retweet
from bot import readCSV,writeCSV,retweet_latest
from pull_new_followers import updateFollowing


def Authenticate(file_name):
  with open(file_name) as f:
    params=json.load(f)
  auth = tweepy.OAuthHandler(params["consumer_key"], params["consumer_secret"])
  auth.set_access_token(params['access_token'], params["access_token_secret"])
  return tweepy.API(auth)


if __name__=="__main__":
  api=Authenticate('./keys.json')
  if os.path.isfile('dict.csv'):
    pass
  else:
    os.mkdir('dict.csv')
  updateFollowing("dict.csv")
  check_last_retweet('dict.csv')
  retweet_latest('dict.csv')
  

