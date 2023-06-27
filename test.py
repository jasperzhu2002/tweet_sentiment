import transformers
import torch
from transformers import GPTNeoForCausalLM, GPT2Tokenizer

model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")

prompt = (
    f"""
    Please rate the sentiment of the following tweet, 
    which is delimited with triple backticks. Respond with
    only an integer from 1 to 10, where one is the worst and 10
    is the best.`

    Review text: '''Ethereum is good!'''
    """
)

input_ids = tokenizer(prompt, return_tensors="pt").input_ids

gen_tokens = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.9,
    max_length=100,
)
gen_text = tokenizer.batch_decode(gen_tokens)[0]

print(gen_text)