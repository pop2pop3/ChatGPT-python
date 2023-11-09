import cv2  # We're using OpenCV to read video
import base64
import time
import os
import requests
from openai import OpenAI
from datetime import datetime
from IPython.display import display, Image, Audio
from imgcat import imgcat

api_key = open("api_key_location/api_key.txt").read().strip()
client = OpenAI(api_key=api_key)
chat_completion = client.chat.completions

def gpt_4_vision_media(media, query: str):
    r"""
    Implementation of GPT's visual capabilities from video.

    `media`: video location.

    `query`: your query about the video.
    """
    video = cv2.VideoCapture(media)
    base64Frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
    video.release()
    print(len(base64Frames), "frames read.")
    display_handle = display(None, display_id=True)
    for img in base64Frames:
        display_handle.update(Image(data=base64.b64decode(img.encode("utf-8"))))
        time.sleep(0.025)

    PROMPT_MESSAGES = [
    {
        "role": "user",
        "content": [
            query, # Example: These are frames from a video that I want to upload. Generate a compelling description that I can upload along with the video.
            *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::10]),
        ],
    },
    ]
    params = {
        "model": "gpt-4-vision-preview",
        "messages": PROMPT_MESSAGES,
        "api_key": os.environ[api_key],
        "headers": {"Openai-Version": "2020-11-07"},
        "max_tokens": 300,
    }

    result = chat_completion.create(**params)
    return result.choices[0].message.content

def gpt_4_vision_mediaurl(image_url, query) -> str:
    r"""
    Implementation of GPT's visual capabilities from image from external URL.
    The image will be encoded to base64 format before taking as the input to the model

    `image_url`: image URL.

    `query`: your query about the video.
    """
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": image_url,
                },
            ],
        }
    ],
    max_tokens=500,
    )

    return response.choices[0].message.content

def gpt_4_vision_localmedia(file_location, query) -> str:
    r"""
    Implementation of GPT's visual capabilities from an image.
    The image will be encoded to base64 format before taking as the input to the model

    `file_location`: image file location.

    `query`: your query about the video.
    """

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image
    image_path = file_location

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": query
            },
            {
                "type": "image_url",
                "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
            ]
        }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']

#EXAMPLE
"""
if __name__ == "__main__":
    print(gpt_4_vision_mediaurl("https://akcdn.detik.net.id/community/media/visual/2022/11/25/indomie-bangladesh-3.jpeg?w=3487", "Give me the description of the food and create the recipe, and anyway where did this image taken from originally?"))
"""
