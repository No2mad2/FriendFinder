#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, re
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.api import API
CONSUMER_KEY = 'xxx'
CONSUMER_SECRET = 'xxx'
ACCESS_KEY = 'xxx-xxx'
ACCESS_SECRET = 'xxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#Authentication is out of the way
#This app has read-only permission, as to not accidentally post or annoy anyone
class StdOutListener(StreamListener):

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        try:#try to get geolocation
            print ('@%s: %s %s' % (decoded['user']['screen_name'], decoded['geo']['coordinates'], decoded['text'].encode('ascii', 'ignore')))
        except:#if we cant, just print the text
            print ('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
            #pass - remove this line if you want to ignore the tweet, and only grab geolocation enabled tweets
        return True

if __name__ == '__main__':

    l = StdOutListener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    stream = Stream(auth, l, timeout=None, compression=True) # Words to search for in the stream
    stream.filter(track = ['follow me on insta ', 'snapchat me: ', 'text me: ', 'add me on snapchat: ', 'follow me on instagram: ', 'text me ('])
