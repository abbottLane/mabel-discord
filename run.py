from app.discord_bot.connect_discord import client, discord_token

if  __name__ == '__main__':
    print("Starting Discord Bot")
    # run the discord bot on port 8080
    client.run(discord_token)