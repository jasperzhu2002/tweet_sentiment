import pandas as pd
from GetSentiment import get_sentiment

def sortData(tweets, username, keyword):
    # filter rows
    filtered_tweets = tweets[(tweets['Text'].str.contains(keyword))] # | (tweets['Hashtags'].str.contains(keyword))]

    # creates sentiment data frame
    sentiments = pd.DataFrame.from_dict({'Score': []})
    # fills in the DFs
    for index, row in filtered_tweets.iterrows():
        sentiment = get_sentiment(row[1])
        sentiments.loc[row[0]] = [sentiment]

    # moves data to CSV and returns
    sentiments.to_csv(f'./output/{username}_sorted.csv')
    return sentiments