# pip3 install transformers
from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
text = "Hello, how are you?"
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print(f"Tokens: {tokens}")
print(f"Token IDs: {token_ids}")
