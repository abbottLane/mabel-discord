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
        if message.author == self.user:
            return
        message_content=message.content
        chat_response=chatgpt_response(message_content)
        if "mabel" in message_content.lower() or "Mabel" in message_content.lower():
            print(message_content)
            await message.channel.send(f"{chat_response}")
        return 
intents=discord.Intents.default()
intents.messages=True
client=MyClient(intents=intents)
