from Pipeline import pipe
import numpy as np

def get_sentiment(tweet):
    res = pipe(tweet)

    return res[0] * 1 + res[1] * 2 + res[2] * 3