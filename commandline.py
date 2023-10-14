#!/usr/bin/python3
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import os
from decouple import config

# Load the bot token from the .env file
TOKEN = config('TOKEN')

# Create the bot and updater as you did before
bot = telegram.Bot(
    token=TOKEN, request=telegram.utils.request.Request(con_pool_size=8))

updater = Updater(bot=bot, use_context=True)

# Import command handlers from separate files
from commands import (
    directory_commands,
    file_commands,
    general_commands,
    text_commands,
)

# Add command handlers from separate files
updater.dispatcher.add_handler(CommandHandler('start', general_commands.start))
updater.dispatcher.add_handler(CommandHandler('help', general_commands.help))
updater.dispatcher.add_handler(CommandHandler('make_directory', directory_commands.make_directory))
updater.dispatcher.add_handler(CommandHandler('list_files', directory_commands.list_files))
updater.dispatcher.add_handler(CommandHandler('change_directory', directory_commands.change_directory))
updater.dispatcher.add_handler(CommandHandler('delete_dir', directory_commands.delete_dir))
updater.dispatcher.add_handler(CommandHandler('print_file', file_commands.print_file))
updater.dispatcher.add_handler(CommandHandler('display_txt', file_commands.display_txt))
updater.dispatcher.add_handler(CommandHandler('open_file', file_commands.open_file))
updater.dispatcher.add_handler(CommandHandler('new_file', file_commands.new_file))
updater.dispatcher.add_handler(CommandHandler('delete_file', file_commands.delete_file))
updater.dispatcher.add_handler(CommandHandler('echo', text_commands.echo))
updater.dispatcher.add_handler(CommandHandler('cat', text_commands.cat))
updater.dispatcher.add_handler(CommandHandler('vi', text_commands.vi))
updater.dispatcher.add_handler(CommandHandler('touch', text_commands.touch))

# Add more command handlers from other categories
def reply_to_text(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    from commands import (
        directory_commands,
        file_commands,
        general_commands,
        text_commands,
    )

    commands = {
            "help": help,
            "yes": help,
            "yeah": help,
            "sure": help,
            "yes please": help,
            "make directory": make_directory,
            "delete file": delete_file,
            "list files": list_files,
            "change directory": change_directory,
            "check path": check_path,
            "display text": display_txt,
            "print file": print_file,
            "open file": open_file,
            "new file": new_file,
            "delete file": delete_file,
            "delete directory": delete_dir,
            "echo": echo,
            "cat": cat,
            "vi": vi,
            "touch": touch,
        }

    # Check if the text is a recognized command
    if text in commands:
        commands[text](update, context)
    elif text == "thank you":
        update.message.reply_text("You're welcome!")
    else:
        update.message.reply_text("Sorry, I didn't understand that.")    # Handle normal text responses
    text = update.message.text.lower()

# Keep the MessageHandler for normal text messages
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply_to_text))

# Start polling
updater.start_polling()

