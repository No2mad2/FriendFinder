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

try:
    status = api.get_status (id='tweet_id_here')
    print status.geo #Print exact geo coordinates, prints none if location not used
except Exception,e: print str(e)
