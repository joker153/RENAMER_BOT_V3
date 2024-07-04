import logging
from pyrogram import Client, idle
from info import TOKEN, API_ID, API_HASH, STRING
from plugins.cb_data import app as Client2

# Configure logging
logging.basicConfig(level=logging.INFO)

# Function to clear session files
def clear_session_files(session_name):
    try:
        os.remove(f"{session_name}.session")
        logging.info(f"Session file {session_name}.session removed successfully.")
    except FileNotFoundError:
        logging.info(f"No session file named {session_name}.session found.")

# Initialize the main bot client
bot = Client(
    "Renamer",
    bot_token=TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

def start_clients(apps):
    for app in apps:
        try:
            app.start()
            logging.info(f"{app} started successfully.")
        except Exception as e:
            if "unpack requires a buffer of 271 bytes" in str(e):
                logging.error("Session file corrupted. Clearing session files and re-authenticating.")
                clear_session_files(app.session_name)
                app.start()
            else:
                logging.error(f"An error occurred while starting {app}: {e}")

def stop_clients(apps):
    for app in apps:
        try:
            app.stop()
            logging.info(f"{app} stopped successfully.")
        except Exception as e:
            logging.error(f"An error occurred while stopping {app}: {e}")

try:
    if STRING:
        # If STRING is set, start both clients
        apps = [Client2, bot]
        start_clients(apps)
        idle()
        stop_clients(apps)
    else:
        # If STRING is not set, run the main bot client
        bot.run()
        logging.info("Bot started successfully.")
except Exception as e:
    logging.error(f"An error occurred: {e}")
