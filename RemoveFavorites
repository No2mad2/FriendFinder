import tweepy, time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.api import API
CONSUMER_KEY = 'xxx'
CONSUMER_SECRET = 'xxx'
ACCESS_KEY = 'xxx'
ACCESS_SECRET = 'xxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)  
x = 0 #Used for keeping rough count of tweets unfavoritied
while True:
    try:
        for status in tweepy.Cursor(api.favorites).items(200):
            #print status.id
            api.destroy_favorite(status.id)
            print 'deleted favorite %s' % (status.id)
            x += 1
            print 'Tweets unfavorited: %s' % (x)
            time.sleep(30)
    except:
        time.sleep(700) #If we hit rate limit, wait it out
        pass
