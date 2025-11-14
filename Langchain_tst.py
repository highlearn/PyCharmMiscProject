from ollama import chat  # Install via: pip install ollama

def ask_gemma3(prompt: str, model: str = "gemma3:1b"):
    response = chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    # response.message.content works too if using the ChatResponse object
    print("Model response:", response["message"]["content"])

if __name__ == "__main__":
    ask_gemma3("Write a short poem about autumn leaves.", model="gemma3:1b")