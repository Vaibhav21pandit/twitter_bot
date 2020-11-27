###This script looks for the latest tweet of a particular user,retweets it and store the last tweet id.
import tweepy
import os
import json
import requests
import urllib
import csv
from bot import readCSV,writeCSV 

with open('./keys.json') as f:
    params=json.load(f)
auth = tweepy.OAuthHandler(params["consumer_key"], params["consumer_secret"])
auth.set_access_token(params['access_token'], params["access_token_secret"])
api=tweepy.API(auth)


def check_last_retweet(csv):
  new_dict={}
  r=0
  since_ids=readCSV(csv)
  for user,id in since_ids.items():
    print(user,id)
    if str(id)=="0":
      try:
        # print(user,id)
        post=api.user_timeline(user,count=1)
        retweet_id=post[0].id
        api.retweet(retweet_id)
        new_dict[user]=retweet_id
        r+=1
      except:
        new_dict[user]=(api.user_timeline(user,count=2)[1].id) 
    else:
      new_dict[user]=(api.user_timeline(user,count=2)[1].id)
  writeCSV(new_dict)
  print(f'{r} tweets retweeted and users added')

check_last_retweet('./dict.csv')

