from app.discord_bot.connect_discord import client, discord_token

if  __name__ == '__main__':
    print("Starting Discord Bot")
    client.run(discord_token)