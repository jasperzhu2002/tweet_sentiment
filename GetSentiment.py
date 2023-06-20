from Pipeline import pipe

def get_sentiment(tweet):
    res = pipe(tweet)[0]

    # determine pos/neg/neutral
    if res['label'] == 'LABEL_0':
        score = -1 - (2 * res['score'])
    elif res['label'] == 'LABEL_1':
        score = (res['score'] - 0.5) * 2
    else:
        score = 1 + (2 * res['score'])
    
    return score