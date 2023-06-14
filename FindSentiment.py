import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPEN_AI_KEY')
openai.api_base = os.getenv('OPEN_AI_ENDPOINT')
openai.api_type = 'azure'
openai.api_version = '2023-03-15-preview'

# gets the chat gpt reponse
def get_completion(prompt, deployment_name='gpt35'):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message.content

# uses chatGPT to get sentiment
def get_sentiment(tweet):
    prompt = f"""
    What is the sentiment of the following tweet, 
    which is delimited with triple backticks? Please rate
    the sentiment from 1 to 10 where 1 is the worst and
    10 is the best. Please respond with only the rating
    as an integer.

    Review text: '''{tweet}'''
    """
    response = get_completion(prompt)

    return response