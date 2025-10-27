from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)


chatbot_prompt = (
    "You are a friendly AI assistant. "
    "Answer the user's question with a detailed response, giving multiple facts or examples."
)

messages = [{"role": "user", "content": "Tell me some interesting facts about electricity."}]

response = generator(
    f"{chatbot_prompt} {messages[-1]['content']}",
    max_new_tokens=500,
    do_sample=True,
    temperature=0.7
)

print(response[0]["generated_text"])