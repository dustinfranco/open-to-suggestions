import twitter
import twitter_config as tc
api = twitter.Api(
consumer_key = tc.tapi,
consumer_secret = tc.tapis,
access_token_key = tc.tat,
access_token_secret = tc.tats
)
def get_tweets(get_number = 1):
  #print(api.VerifyCredentials())
  mentions = api.GetMentions(count = get_number)
  return mentions

