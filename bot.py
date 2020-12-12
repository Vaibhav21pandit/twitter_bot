###Remember in terminal some keys/words have spaces between,just replace those spaces with '_' ###
import tweepy
import os
import json
import requests
import urllib
import csv

with open('./keys.json') as f:
    params=json.load(f)
auth = tweepy.OAuthHandler(params["consumer_key"], params["consumer_secret"])
auth.set_access_token(params['access_token'], params["access_token_secret"])
api=tweepy.API(auth)

#writing the names of users and their last tweet id
def writeCSV(dicty):
  with open('dict.csv', 'w') as csv_file:  
      writer = csv.writer(csv_file)
      for key, value in dicty.items():
        writer.writerow([key, value])

###importing JSON and checking last tweet id###
def readCSV(fname):
  with open(fname) as csv_file:
      reader = csv.reader(csv_file)
      return dict(reader)

# using the already tweeted ids to retweet only the new ones and updating the since_Ids dict
def post_latest(csv):
  retweets=0
  new_dict={}
  since_ids=readCSV(csv)
  for user,id in since_ids.items():
    post=api.user_timeline(user,since_id=id,count=1)
    try:
      if len(post)!=0 and post[0].__dict__['_json']['extended_entities']['media'][0]['type']=="video":
        api.update_status(post[0].__dict__['_json']['entities']['media'][0]['expanded_url'])
        retweets+=1
        new_dict[user]=retweet_id
      else:
        new_dict[user]=id
    except:
        new_dict[user]=id
  print(f'Posted {retweets} new tweets!!! ')
  writeCSV(new_dict)


if __name__=='__main__':  
  post_latest('dict.csv')
  





###### Different API Experiments #######
# public_tweets = api.home_timeline()
# public_tweets=api.home_timeline()

# print(type(public_tweets))

# for tweet in public_tweets:
#   # print(tweet.text)
#   if "teen" or "anal" in tweet.text.lower():
#     print(tweet.text,tweet.id)


# posts=api.user_timeline('mayaunmoor',count=1)
# id=posts[0].id
# posts=posts[0].__dict__
# dwn_link =(posts['_json']['entities']['media'][0]['id_str'])
# print(dwn_link)
# api.retweet(id)
# https://twitter.com/mayaunmoor/status/1331606895149289474
# file_name = './trial_video.mp4' 
# urllib.request.urlretrieve(dwn_link, file_name)

# api.media_upload('trial_video.mp4',status="Steaming Hot")
# api.update_status('https://imgur.com/2swt4ZW')
