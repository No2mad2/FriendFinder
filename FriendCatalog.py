#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, re
from tweepy import OAuthHandler
from tweepy.api import API
from sys import argv
CONSUMER_KEY = 'xxx'
CONSUMER_SECRET = 'xxx'
ACCESS_KEY = 'xxx-xxx'
ACCESS_SECRET = 'xxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)  

c = tweepy.Cursor(api.search, q='searchterm', include_entities=True).items() #change searchterm

# Catalog Function
# Will slowly archive every tweet.
# Might be dangerous on some users who have
# very high tweet counts.

f = open('Text', 'a')

def cata(wait = 10): #catalog function
    tweet = c.next()
    f.write('@%s Location: %s %s Client: %s Created: %s %s\n' % (tweet.user.screen_name, str(tweet.geo), tweet.user.profile_image_url, tweet.source, tweet.created_at, tweet.text))
    wait = time.sleep(wait)
    return;
    
while True:
    try:
        cata()
    except:
        pass
    
