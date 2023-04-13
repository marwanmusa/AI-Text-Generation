# Import Dependencies
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch
import warnings
warnings.filterwarnings('ignore')

# Load Model
device = 'cuda'
model_name = 'EleutherAI/gpt-neo-2.7B'
tokenizer = GPT2Tokenizer.from_pretrained(model_name, cache_dir = "cache/")
model = GPTNeoForCausalLM.from_pretrained(model_name, cache_dir = "cache/", pad_token_id=tokenizer.eos_token_id).to(device)

# Create function to generate text
def generate(text, max_len):
    # Input sentences and tokenize it
    input_ids = tokenizer(text, return_tensors='pt').input_ids
    # input_ids = input_ids.to(device)

    # Generate sentences
    gen = model.generate(input_ids,
                         do_sample = True,
                         temperature = 0.9,
                         max_length = max_len)
    gen_text = tokenizer.batch_decode(gen)[0]
    return gen_text

while True:
    print("AI Text Generation with GPT-Neo-2.7B")
    text = input('Prompt:')
    text_length = int(input('Text length:'))
    print(generate(text, text_length))
    next_ = input("Generate Again - yes/no:")
    if next_.lower() == 'no':
        break