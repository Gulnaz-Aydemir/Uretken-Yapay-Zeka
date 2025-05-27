from transformers import GPT2LMHeadModel, GPT2Tokenizer


model_name = "gpt2"  # GPT-2 modelini kullanıyoruz
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

print("Model ve Tokenizer başarıyla yüklendi!")
