from dotenv import load_dotenv
import os
import discord
from app.mabel.connect_openai import chatgpt_response

load_dotenv()
discord_token=os.getenv('DISCORD_TOKEN')
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as: ', self.user)
    async def on_message(self, message):
        if message.author == self.user:
            return
        chat_response=chatgpt_response(message.content)
        if "mabel" in message.content.lower() or "Mabel" in message.content.lower():
            print(message.content)
            await message.channel.send(f"{chat_response}")
        return 
intents=discord.Intents.default()
intents.messages=True
client=MyClient(intents=intents)
