import tweepy
from textblob import TextBlob
import configs

class Twitter:

    def __init__(self):
        # Authenticate to Twitter
        CONSUMER_KEY = configs.CONSUMER_KEY
        CONSUMER_SECRET = configs.CONSUMER_SECRET
        ACCESS_TOKEN = configs.ACCESS_TOKEN
        ACCESS_TOKEN_SECRET = configs.ACCESS_TOKEN_SECRET

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        # Create API object
        self.api = tweepy.API(auth, wait_on_rate_limit=True,
                              wait_on_rate_limit_notify=True)
        try:
            self.api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

    def api_obj(self):
        return self.api

    def convert_tweet_to_dict(self, tweet):
        analysis = TextBlob(tweet.text)
        dic = {"tweet_id": tweet.id_str,
               "user_id": tweet.user.id_str,
               "tweet_date": tweet.created_at,
               "text": tweet.text.encode('ascii', 'ignore').decode('ascii'),
               "name": tweet.user.name.encode('ascii', 'ignore').decode('ascii'),
               "user_name": tweet.user.screen_name,
               "location": tweet.user.location,
               "followers_count": tweet.user.followers_count,
               "polarity": analysis.polarity
               }
        return dic

    def retrieve_tweets_by_keyword(self, searchWord):
        return self.api.search(q=searchWord, lang="en", rpp=10)


def clean_dic(dic):
    result = {}
    for key, value in dic.items():
        if value is None:
            value = ''
        result[key] = value
    return result
