#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, re
from tweepy import OAuthHandler
from tweepy.api import API
from sys import argv
CONSUMER_KEY = 'xxx'
CONSUMER_SECRET = 'xxx'
ACCESS_KEY = 'xxx'
ACCESS_SECRET = 'xxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

c = tweepy.Cursor(api.home_timeline).items() #Set up cursor

def cata(wait = 10): # Different catalog function
    tweet = c.next()
    print ('@%s Location: %s %s Client: %s Created: %s %s\n' % (tweet.user.screen_name, str(tweet.geo), tweet.user.profile_image_url, tweet.source, tweet.created_at, tweet.text))
    wait = time.sleep(wait)
    return 0

while True:
    try:
        cata()
    except:
        pass
