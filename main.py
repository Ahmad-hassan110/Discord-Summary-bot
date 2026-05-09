import os
from dotenv import load_dotenv
from bot.discord_client import bot

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

if __name__ == '__main__':
    print("Starting the bot initialization...")
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("Error: No Discord token found.")