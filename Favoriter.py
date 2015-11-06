import tweepy, random
from random import randint

auth = tweepy.OAuthHandler("xxx", "xxx")
auth.set_access_token("xxx", "xxx")

api = tweepy.API(auth)

searches = api.search("searchterm", count=100) #Change searchterm
for tweet in searches:
    result = (randint(0,10))
    print(result)
    limits = api.rate_limit_status()
    remain_search_limits = limits['resources']['search']['/search/tweets']['remaining']
    #print(remain_search_limits)
    #print tweet.text.encode('utf8') - Might cause errors if emojis are printed
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
    # Remove comments for random retweets from new favorites
