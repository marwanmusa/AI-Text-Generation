# Text Generation using GPT-Neo and GPT2
***Build Text Generator*** app with ***GPT-Neo by [EleutherAI](https://github.com/EleutherAI)*** and ***GPT2 by [OpenAI](https://github.com/openai)*** using ***Transformer***.

Source :
1. GPT-Neo : [Github](https://github.com/EleutherAI/gpt-neo), [HuggingFace](https://huggingface.co/docs/transformers/model_doc/gpt_neo)
2. GPT2 : [Github](https://github.com/openai/gpt-2), [HuggingFace](https://huggingface.co/docs/transformers/model_doc/gpt2)
3. Transformers - Text Generation Strategies : [HuggingFace](https://huggingface.co/docs/transformers/generation_strategies)

How to run:
1. Clone this repository
```python
git clone https://github.com/marwanmusa/AI-Text-Generation.git
```
2. Make virtual environment on your local directory
```python
python -m venv "your_env_name"
```
3. Activate the environment
```python
"your_env_name"/Scripts/Activate.ps1
```
4. Install dependencies in *requirements.txt*
```python
pip install -r path/to/requirements.txt
```
or if you are using pipenv, then
```python
pipenv install -r path/to/requirements.txt
```
5. Run `.py` files
```python
python text_generator_with_gpt_Neo.py # for GPTNeo
python text_generator_with_gpt2.py # for GPT2
```
