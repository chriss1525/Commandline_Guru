#!/usr/bin/python3
import telegram
from telegram.update import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import telegram.ext
import spacy
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

print(token)
# bot = telegram.Bot(token=token)
# nlp = spacy.load("en_core_web_sm")

updater = telegram.ext.Updater(token, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello there need help with the terminal?")


updater.dispatcher.add_handler(CommandHandler('start', start))


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        """
        Available commands :- 
        /make_directory - how to create a new directory
        /empty_file - how to create an empty file
        /list_files - how to list files in your currenct directory
        /check_directory - how to check what directory you're in
        /change_directory - how to change your current directory
        /repository - how to create a new repository
        """)


updater.dispatcher.add_handler(CommandHandler('help', help))


def make_directory(update: Update, context: CallbackContext):
    # get user's message
    # user_message = update.message.text
    # process user message

    # logic to create a new directory
    update.message.reply_text(
        "To create a new directory, use the `mkdir` command followed by the name of the directory you want to create. For example, to create a directory called 'my_directory', you can run the following command in your terminal:\n\n"
        "```\n"
        "mkdir my_directory\n"
        "```\n"
        "This will create a new directory named 'my_directory' in your current working directory.")


updater.dispatcher.add_handler(
    CommandHandler('make_directory', make_directory))


def change_directory(update: Update, context: CallbackContext):
    # logic to navigate the terminal
    update.message.reply_text(
        "To change directories, use the `cd` command to change directory.")


updater.dispatcher.add_handler(CommandHandler(
    'change_directory', change_directory))


def reply_to_text(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    if text == "yes":
        # Send help message
        help(update, context)

    if text == "make directory":
        # create new directory
        make_directory(update, context)

    elif text == "thank you":
        # Send thank you message
        update.message.reply_text("You're welcome!")

    else:
        # Send default response
        update.message.reply_text("Sorry, I didn't understand that.")


updater.dispatcher.add_handler(MessageHandler(Filters.text, reply_to_text))

updater.start_polling()
