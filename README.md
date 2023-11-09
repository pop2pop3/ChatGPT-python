# ChatGPT-python
ChatGPT Python simple program that you can develop into a project that suits your preferences and needs.

This code is based on the assumption that the ChatGPT API will function similarly to the GPT-3 API. 
But with some differences in how the conversation is structured. 
ChatGPT API is available with variety of models like GPT 3.5 or GPT-4 (if you already have access to the API), you'll need to replace the `chatgpt-model-id` placeholder with the actual model ID and make any necessary adjustments based on the official API documentation.

Here's a basic implementation of a chatbot using OpenAI's ChatGPT and the `openai` Python library. This example demonstrates how to maintain context during a conversation by continuously updating the conversation history. You'll need to have an OpenAI API key to use this example:

First, install the required library:

```bash
pip install openai -U
```
Run ```main.py``` or ```streaming.py``` by ```python3 main.py``` or ```python3 streaming.py```
That's it!

# GPT-4-VISION (Updated)

GPT-4 with Vision, sometimes referred to as GPT-4V or gpt-4-vision-preview in the API, allows the model to take in images and answer questions about them. Historically, language model systems have been limited by taking in a single input modality, text. For many use cases, this constrained the areas where models like GPT-4 could be used.

GPT-4 with vision is currently available to all developers who have access to GPT-4 via the ```gpt-4-vision-preview``` model and the Chat Completions API which has been updated to support image inputs.

We welcome contributions. If you have an idea for a new feature or have found a bug, please open an issue on the GitHub repository.
