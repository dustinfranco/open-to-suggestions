#!/usr/bin/env python
import time
import typewriter.get_tweets as gt
import typewriter.suggestions_main as sm

sm.gpio_setup()
sm.clear_pins()

last_tweet = ""

c_buf = 0
#if its the exact len it causes funny issue:
p_tweets = []

while(1):
  try:
    printed_tweet = False
    print("getting tweets")
    tweets = gt.get_tweets(10)
    print("\n\n\n\n")
    for tweet in tweets:
      if(tweet.id not in p_tweets):
        printed_tweet = True
        p_tweets.append(tweet.id)
        print("found new tweet: " + tweet.text)
        tweet.text = tweet.text.replace("@SuggestionsPrnt", "")
        if(tweet.text.find("http")):
          tweet.text = tweet.text[0:tweet.text.find("http")]
        sm.t_print_string("////////\n")
        sm.t_print_string(tweet.user.screen_name + "\n")
        sm.t_print_string(tweet.text + "\n")
    if not printed_tweet:
      print("no unique tweets")
      time.sleep(10)
  except Exception as e:
      print(e)

