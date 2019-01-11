import twitter
import os
env_vars = os.environ
api = twitter.Api(
consumer_key = env_vars["twitter_key"],
consumer_secret = env_vars["twitter_secret_key"],
access_token_key = env_vars["twitter_token"],
access_token_secret = env_vars["twitter_token_secret"]
)
def get_tweet():
  #print(api.VerifyCredentials())
  mentions = api.GetMentions(count = 1)
  for tweet in mentions:
    print(tweet.text)
    print(tweet.text.replace("@SuggestionsPrnt",""))


