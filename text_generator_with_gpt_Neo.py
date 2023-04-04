# Import Dependencies
from transformers import pipeline
import warnings
warnings.filterwarnings('ignore')

# Load Model
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# Create function to generate text
def generate(text, text_length):
    # Input text to generator
    output = generator(text, max_length=text_length, do_sample=True, temperature=0.9)

    # Output result
    text = output[0]['generated_text']
    return text

while True:
    print("AI Text Generation with GPT-Neo-2.7B")
    text = input('Prompt:')
    text_length = int(input('Text length:'))
    print(generate(text, text_length))
    next_ = input("Generate Again:")
    if next_.lower() == 'no':
        break