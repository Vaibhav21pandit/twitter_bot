import praw
import requests
import urllib
import json
# import re

scrape_link = "https://redgifs.com/watch/fatherlytalkativeicterinewarbler"
dwn_link="https://thumbs.redgifs.com/FatherlyTalkativeIcterinewarbler-mobile.mp4"
file_name = 'trialVideo.gif' 


headers = {'user-agent': 'my-app/0.0.1'}
content=requests.get(dwn_link,headers=headers)

with open("trialvid.gif","wb") as f:
  f.write(content.content)



with open('./keys.json') as f:
  parameters=json.load(f)

reddit = praw.Reddit(client_id=parameters['client_id'],
                     client_secret=parameters['client_secret'],
                     password=parameters['password'],
                     user_agent=parameters["user_agent"],
                     username=parameters["username"])

print(reddit.user.me())
subreddit = reddit.subreddit('PornoCasino')

for submission in (subreddit.hot(limit=10)):
  print(submission.url)

def deEmojify(inputString):
    returnString = ""

    for character in inputString:
        try:
            character.encode("ascii")
            returnString += character
        except UnicodeEncodeError:
            replaced = unidecode(str(character))
            if replaced != '':
                returnString += replaced
    
    return " ".join(returnString.split()) #removes double spaces after replacing an emoji


########################################################DUMP#################################################
# from urllib.request import Request, urlopen, urlretrieve

# req = Request(dwn_link, headers={'User-Agent': 'Mozilla/5.0'})
# print(req.full_url)
# urlretrieve(req.full_url,'trial_video.mp4')

# scrape=requests.get(dwn_link)
# print(scrape)
# from bs4 import BeautifulSoup
# bs=BeautifulSoup(scrape.text.encode('utf-8'), "html.parser")
# for link in bs.find_all('a') :
#     if link.has_attr('href'):
#         print (link.attrs['href'])