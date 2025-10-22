from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

print("Chatbot bereit! (Tippe 'bye' zum Beenden)\n")

while True:
    user_input = input("Du: ").strip()

    if user_input.lower() in ["bye", "tschüss", "exit", "quit"]:
        print("Bot: Tschüss! ")
        break
    elif not user_input:
        print("Bot: Bitte schreibe etwas.")
        continue

    response = generator(
        user_input,
        max_new_tokens=100,
        num_beams=5,
        no_repeat_ngram_size=3,
        repetition_penalty=2.0,
        early_stopping=True
    )

    print("Bot:", response[0]["generated_text"])
