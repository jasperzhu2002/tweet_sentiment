import pandas as pd
from FindSentiment import get_sentiment

def sortData(tweets, username, keyword):
    # filter rows
    filtered_tweets = tweets[(tweets['Text'].str.contains(keyword)) | (tweets['Hashtags'].str.contains(keyword))]

    # creates sentiment data frame
    sentiments = pd.DataFrame.from_dict({'Score': []})
    # fills in the DF
    for index, row in filtered_tweets.iterrows():
        sentiment = get_sentiment(row[1])
        sentiments.loc[row[0]] = [sentiment]
        print(index)

    # moves data to CSV and returns
    sentiments.to_csv(f'./output/{username}_sorted.csv')
    return sentiments