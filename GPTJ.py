# Import Dependencies
from transformers import GPTJForCausalLM, AutoTokenizer
import torch


# load Model
device = 'cuda'
model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", torch_dtype=torch.float16, cache_dir='cache/').to(device)
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B", cache_dir='cache/')

# Create function to generate text
def generate(text, max_len):
    # Input sentences and tokenize it
    input_ids = tokenizer(text, return_tensors='pt').input_ids.to(device)

    # Generate sentences
    gen = model.generate(input_ids,
                         do_sample = True,
                         temperature = 0.9,
                         max_length = max_len)
    gen_text = tokenizer.batch_decode(gen)[0]
    return gen_text

while True:
    print("AI Text Generation with GPT-J")
    text = input('Prompt:')
    text_length = int(input('Char length:'))
    print(generate(text, text_length))
    next_ = input("Generate Again - YES/NO:")
    if next_.lower() == 'no':
        break