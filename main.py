import openai

with open("path-to-file/openai_api_key.txt") as key: # I use this method for a sake of organizing many API keys in a personal directory that I used in my projects
    api_key = key.read()
openai.api_key = api_key

def chat_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use the appropriate ChatGPT model ID
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message['content'].strip()

def main():
    conversation_history = []
    user_input = ""

    print("Welcome to the Chatbot! Type 'quit' to exit.")

    while user_input.lower() != "quit":
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        conversation_history.append({"role": "user", "content": user_input})

        # Send the conversation history to ChatGPT
        prompt = "\n".join([message["content"] for message in conversation_history])  # Update this line
        response = chat_chatgpt(prompt)

        print(f"Chatbot: {response}")

        # Update the conversation history
        conversation_history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
