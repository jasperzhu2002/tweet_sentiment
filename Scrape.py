import sys
import os
from datetime import datetime
import pandas as pd
import snscrape.modules.twitter as sntwitter

def scrape(username, limit):
    old_stdout = sys.stdout
    sys.stdout = open(os.devnull, "w")

    tweets = []
    date_limit = datetime(2022, 1, 1)
    counter = 0

    try:
        # scrapes the tweets
        for i, tweet in enumerate(sntwitter.TwitterProfileScraper(username).get_items()):
            unaware_tweet_date = tweet.date.replace(tzinfo=None)
            # check dates
            if date_limit > unaware_tweet_date:
                counter += 1
            elif len(tweet.content) > 100:
                pass
            else:
                # appends tweet
                tweets.append([tweet.date, tweet.content, tweet.hashtags])

            # checks for limit
            if i > limit or counter >= 3:
                break
    except:
        sys.stdout = old_stdout
        print("dang :(")

    sys.stdout = old_stdout

    # adding data to DF
    df = pd.DataFrame(tweets, columns=['Datetime', 'Text', 'Hashtags'])

    # converts to Excel and returns
    df.to_csv(f'./data/{username}_tweets.csv')
    return df