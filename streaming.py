import openai

api_key = open("path-to-file/openai_api_key.txt").read() # I use this method for a sake of organizing many API keys in a personal directory that I used in my projects
openai.api_key = api_key

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r,g,b,text)

def chat_chatgpt_stream(prompt):

    r"""
    Implementation of streaming response ChatGPT-style
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use the appropriate ChatGPT model ID
        messages=[{"role": "system", "content": "You are a helpful assistant."}, # Design your system prompt
                  {"role": "user", "content": prompt}],
        max_tokens=150,
        top_p=1,
        stop=None,
        temperature=0.5,
        stream = True,
    )
    # store all collected chunk messages from the loop
    collected_chunk = []

    # loop method to display stream-like ChatGPT token by token
    for chunk in response:
        content = chunk['choices'][0].get('delta', {}).get('content')
        if content is not None:
            # print response with color
            # R=218, G=165, B=32 will produce light orange color
            print(colored(218,165,32, str(content).replace("None", "")), end='', flush=True)
            collected_chunk.append(content.replace("None", ""))
    final_response = "".join(collected_chunk) # Join all collected chunk messages into final response
    return final_response

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
        response = chat_chatgpt_stream(prompt)

        print(f"Chatbot: {response}")

        # Update the conversation history
        conversation_history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
