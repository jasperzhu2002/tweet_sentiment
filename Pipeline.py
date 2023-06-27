from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

# creates model
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def pipe(tweet):
    # gets the scores
    text = preprocess(tweet)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    return scores

    # # returns labels and scores
    # ranking = np.argsort(scores)
    # ranking = ranking[::-1]
    # for i in range(scores.shape[0]):
    #     l = config.id2label[ranking[i]]
    #     s = scores[ranking[i]]
    #     print(f"{i+1}) {l} {np.round(float(s), 4)}")

# import transformers

# model_name = 'cardiffnlp/twitter-roberta-base-sentiment'
# model = transformers.AutoModelForSequenceClassification.from_pretrained(model_name)
# tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)

# def pipe(tweet):
#     use_model = transformers.pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
#     return use_model(tweet)