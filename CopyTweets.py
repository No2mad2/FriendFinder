#TODO
#capture from a variety of accounts
#use timing function to tweet as soon as possible


import tweepy, json, random, time, codecs

#tweepy auth
from tweepy import OAuthHandler
from tweepy.api import API
CONSUMER_KEY = 'xxx'
CONSUMER_SECRET = 'xxx' 
ACCESS_KEY = 'xxx-xxx'
ACCESS_SECRET = 'xxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, compression=True)

#===================================================

filename = open('foo.txt')
f = filename.readlines()
filename.close()

def copytweet():
    randnum = random.randint(900, 3600)
    for line in f:
        for status in tweepy.Cursor(api.user_timeline, id=line).items(1):
            print status.text
            print status.id
            tweetid = status.id
            print 'about to post status'
            api.update_status(status.text)
            print 'posted status'
            print 'sleeping for %s' % (randnum)
            time.sleep(randnum)
            return 1

try:
    copytweet()
except Exception,e: print str(e)
