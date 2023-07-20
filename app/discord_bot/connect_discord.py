from dotenv import load_dotenv
import os
import discord
from app.mabel.connect_openai import chatgpt_response
import logging
logging.basicConfig(level=logging.INFO)

#load_dotenv()
discord_token=os.getenv('DISCORD_TOKEN')
class MyClient(discord.Client):
    async def on_ready(self):
        logging.info('Logged in as: ' + str(self.user))
    async def on_message(self, message):
        logging.info('Message from {0.author}: {0.content}'.format(message))
        if message.author == client.user:
            return
        #if message channel is an DMChannel respond
        if isinstance(message.channel, discord.channel.DMChannel):
          
            try:
                response = await chatgpt_response(message.content)
            except Exception as e:
                logging.info('CHATGPT Error: '+ str(e))
            try:
                logging.info('Response: ' + response)
                await message.channel.send(response)
            except Exception as e:
                logging.info('DISCORD Error: '+ str(e))
            return

intents=discord.Intents.default()
intents.messages=True
client=MyClient(intents=intents)


