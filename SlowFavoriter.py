import tweepy, random, time
from random import randint

auth = tweepy.OAuthHandler("xxx", "xxx")
auth.set_access_token("xxx", "xxx")

api = tweepy.API(auth)

searches = api.search("searchterm", count=100)
for tweet in searches:
    timerand = (randint(60, 120))
    time.sleep(timerand)
    result = (randint(0,10))
    print(result)
    print (timerand)
    #limits = api.rate_limit_status()
    #remain_search_limits = limits['resources']['search']['/search/tweets']['remaining']
    #print(remain_search_limits)
    #print tweet.text.encode('utf8')
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
    
