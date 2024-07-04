import asyncio
import logging
from pyrogram import Client, idle
from info import TOKEN, API_ID, API_HASH, STRING
from plugins.cb_data import app as Client2

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the main bot client
bot = Client(
    "Renamer",
    bot_token=TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

try:
    if STRING:
        # If STRING is set, start both clients
        apps = [Client2, bot]
        for app in apps:
            app.start()
            logging.info(f"{app} started successfully.")
        idle()
        for app in apps:
            app.stop()
            logging.info(f"{app} stopped successfully.")
    else:
        # If STRING is not set, run the main bot client
        bot.run()
        logging.info("Bot started successfully.")
except Exception as e:
    logging.error(f"An error occurred: {e}")
