#!/usr/bin/python3
import telegram
print(telegram.__version__)
import telegram.ext
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters
from telegram.update import Update
bot = telegram.Bot(token='6182445927:AAG1bXLu-ko-ZXnn49NSVQPJtn3nbKSjzaE')

updater = telegram.ext.Updater("6182445927:AAG1bXLu-ko-ZXnn49NSVQPJtn3nbKSjzaE", use_context=True) 


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello there need help with the terminal?")


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Available commands :- 
        /make directory - how to create a new directory
        /empty file - how to create an empty file
        /repository - how to create a new repository
        /navigate - how to navigate the terminal""")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
