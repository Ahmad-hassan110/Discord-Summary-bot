import os
from dotenv import load_dotenv
from keep_alive import keep_alive
from bot.discord_client import bot

# .env file se hidden variables load karna
load_dotenv()

# Token ko variable mein save karna
TOKEN = os.getenv('DISCORD_TOKEN')

if __name__ == '__main__':
    print("Bot ko start kiya ja raha hai...")
    # Bot ko run karna
    if TOKEN:
        keep_alive()
        bot.run(TOKEN)
    else:
        print("Error: .env file mein DISCORD_TOKEN nahi mila!")