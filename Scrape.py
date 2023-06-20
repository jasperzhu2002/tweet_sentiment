import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape(username, limit):
    tweets = []
    # scrapes the tweets
    try:
        for i, tweet in enumerate(sntwitter.TwitterProfileScraper(username).get_items()):
            # checks for limit
            if i > limit:
                break
            # appends tweet
            tweets.append([tweet.date, tweet.content, tweet.hashtags])
    except:
        print('There was error LOL!')
            
    # adding data to DF
    df = pd.DataFrame(tweets, columns=['Datetime', 'Text', 'Hashtags'])

    # converts to Excel and returns
    df.to_csv(f'./data/{username}_tweets.csv')
    return df