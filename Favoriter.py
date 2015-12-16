import tweepy, random
from random import randint

auth = tweepy.OAuthHandler("xxx", "xxx")
auth.set_access_token("xxx", "xxx")
api = tweepy.API(auth)

searches = api.search("searchterm", count=100) #Change searchterm and number returned
for tweet in searches:
    result = (randint(0,10))
    print(result)
    print "Preparing to favorite"
    try:
        print "tweet id %s" % (tweet.id)
        api.create_favorite(tweet.id)
        print "Successfully favorited!"
    except:
        pass

    #if result == 1:
        #api.retweet(tweet.id)
        #print "Reweeted id %s" % (tweet.id)
