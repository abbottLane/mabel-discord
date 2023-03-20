from dotenv import load_dotenv
import os
import discord
from app.mabel.connect_openai import chatgpt_response

#load_dotenv()
discord_token=os.getenv('DISCORD_TOKEN')
print("DISCORD_TOKEN: ", discord_token)
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as: ', self.user)
    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith('!mabel'):
            prompt = message.content[7:]
            response = await chatgpt_response(prompt)
            await message.channel.send(response)

intents=discord.Intents.default()
intents.messages=True
client=MyClient(intents=intents)


