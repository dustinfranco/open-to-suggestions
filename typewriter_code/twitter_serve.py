#!/usr/bin/env python
import time
import typewriter.get_tweets as gt
import typewriter.suggestions_main as sm

sm.gpio_setup()
sm.clear_pins()

last_tweet = ""

c_buf = 0
p_tweets = [""] * 10

while(1):
  try:
    p_c_buf = c_buf
    tweets = gt.get_tweets(10)
    print("\n\n\n\n")
    for tweet in tweets:
      if(tweet.text not in p_tweets):
        p_tweets[c_buf] = tweet.text
        c_buf += 1
        if(c_buf == len(p_tweets) - 1):
          c_buf=0
        tweet.text = tweet.text.replace("@SuggestionsPrnt", "")
        if(tweet.text.find("http")):
          tweet.text = tweet.text[0:tweet.text.find("http")]
        sm.t_print_string("////////\n")
        sm.t_print_string(tweet.user.screen_name + "\n")
        sm.t_print_string(tweet.text + "\n")
    if(p_c_buf == c_buf):
      print("no unique tweets")
      time.sleep(10)
  except Exception as e:
      print(e)

