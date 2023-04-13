# Import Dependencies
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load Model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large', cache_dir="cache/")
model = GPT2LMHeadModel.from_pretrained('gpt2-large', pad_token_id=tokenizer.eos_token_id, cache_dir="cache/")

# Create function to generate text
def generate(text, text_length):
    # Input sentences and tokenize it
    input_ids = tokenizer.encode(text, return_tensors='pt')

    # Generate and Decode text
    output = model.generate(input_ids, max_length=text_length, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)

    # Output result
    text = tokenizer.decode(output[0], skip_special_tokens=True)
    return text

while True:
    print("AI Text Generation with GPT2-Large")
    text = input('Prompt:')
    text_length = int(input('Text length:'))
    print(generate(text, text_length))
    next_ = input("Generate Again - yes/no:")
    if next_.lower() == 'no':
        break
