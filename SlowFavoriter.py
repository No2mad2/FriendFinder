import tweepy, random, time
from random import randint

auth = tweepy.OAuthHandler("xxx", "xxx")
auth.set_access_token("xxx", "xxx")
api = tweepy.API(auth)

searches = api.search("searchterm", count=100)  #Replace searchterm with what
for tweet in searches:                          #you want to search for
    timerand = (randint(60, 120))
    time.sleep(timerand)
    result = (randint(0,10))
    print(result)
    print (timerand)
    print "Preparing to favorite"
    try:
        print "tweet id %s" % (tweet.id)
        api.create_favorite(tweet.id)
        print "Successfully favorited!"
    except:
        pass
    # Uncomment if you'd like to retweet randomly as well
    #if result == 1:
        #api.retweet(tweet.id)
        #print "Reweeted id %s" % (tweet.id)
    
