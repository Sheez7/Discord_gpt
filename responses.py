import base64
import requests
from openai import OpenAI
from config import OpenAi_token

client = OpenAI(api_key=OpenAi_token)


def get_response(user_input: str):
    response = client.chat.completions.create(
        model='gpt-4o-2024-08-06',
        messages=[
            {"role": "system", "content": f'{user_input}'}
        ]
    )
    answer = response.choices[0].message.content
    print(answer)
    return answer