import csv
import os
import json
import tweepy
from bot import readCSV,writeCSV

with open('./keys.json') as f:
  params=json.load(f)

auth = tweepy.OAuthHandler(params["consumer_key"], params["consumer_secret"])
auth.set_access_token(params['access_token'], params["access_token_secret"])

api=tweepy.API(auth)


def updateFollowing(csv):
  f=0
  friends=api.friends()
  csv=readCSV(csv)
  dicty=csv.copy()

  for friend in friends:
    if friend.screen_name not in csv.keys():
      dicty[friend.screen_name]=0
      f+=1
  writeCSV(dicty)
  print(f'{f} following updated')


updateFollowing('./dict.csv')