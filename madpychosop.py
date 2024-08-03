import logging
import os
import sys
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Telegram Bot Token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I\'m your 24/7 bot. What can I help you with?')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def error(bot, update, error):
    """Log errors caused by updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            updater.stop()
            break

if __name__ == '__main__':
    main()