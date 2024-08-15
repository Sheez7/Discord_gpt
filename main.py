from discord import Intents, Client, Message
from config import OpenAi_token, bot_token
import requests
import base64
from openai import OpenAI
from responses import get_response

openai_client = OpenAI(api_key=OpenAi_token)

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_input: str) -> None:
    if not user_input:
        print('(Empty message)')
        return

    if is_private := user_input[0] == '?':
        user_input = user_input[1:]

    try:
        response: str = get_response(user_input)
        await message.author.send(reponse) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is online!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    # Проверяем, был ли упомянут бот в сообщении
    if client.user in message.mentions:
        username: str = str(message.author)
        user_message: str = message.content
        channel: str = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        await send_message(message, message.content)

def main():
    client.run(token=bot_token)

if __name__ == '__main__':
    main()