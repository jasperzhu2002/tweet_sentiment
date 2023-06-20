import transformers

model_name = 'cardiffnlp/twitter-roberta-base-sentiment'
model = transformers.AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)

def pipe(tweet):
    use_model = transformers.pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
    return use_model(tweet)