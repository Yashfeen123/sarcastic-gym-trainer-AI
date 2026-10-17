from ollama import Client

client = Client(host="http://localhost:11434")

# Sarcastic Gym Trainer system prompt
messages = [
    {
        "role": "system",
        "content": (
            "You are a sarcastic gym trainer who gets hilariously sarcastic "
            "when someone takes leave, skips a workout, or cheats on their diet. "
            "Mock the excuse, then push the person back on track. "
            "Tease the excuse, never their body or looks. "
            "Reply in 2-3 short sentences with no bullet points. "
            "End every response with a mini challenge, such as: "
            "'20 squats. Now.'"
        )
    }
]

print("Welcome to Sarcastic Gym Trainer AI!")
print("Type 'exit' to stop chatting.\n")

while True:
    question = input("You: ")
    
    if question.lower().strip() == "exit":
        print("AI: Goodbye! Don't skip tomorrow!")
        break
        
    if not question.strip():
        continue

    messages.append({"role": "user", "content": question})

    try:
        completion = client.chat(
            model="qwen3.5:0.8b",
            messages=messages,
            think=False  # Keep think=False to prevent empty responses on this model
        )
        
        # Safely extract response
        answer = getattr(completion.message, "content", "").strip()
        
        if not answer:
            answer = "Did you just drop your weights mid-set? Try asking again."

        print(f"\nAI: {answer}\n")
        messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        print(f"\nError: {e}\n")

