#!/usr/bin/python3
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import telegram.ext
import os
from dotenv import load_dotenv

# load_dotenv()
token = os.getenv('TOKEN')


bot = telegram.Bot(
    token=token, request=telegram.utils.request.Request(con_pool_size=8))

updater = telegram.ext.Updater(bot=bot, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello there need help with the terminal?")


updater.dispatcher.add_handler(CommandHandler('start', start))


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        """
        What do you want to do? Type any of the prompts :- 
        /make_directory - how to create a new directory
        /list_files - how to list files in your currenct directory
        /change_directory - how to change your current directory
        /check_path - how to check the path you are currently in
        /print_file - how to print the contents of a file
        /display_txt - how to display the contents of a file on the terminal
        /open_file - how to open a file on the terminal for editing purposes
        /new_file - how to create an empty file
        /delete_file - how to delete a file in the terminal
        /delete_directory - how to delete an empty directory
        """)


updater.dispatcher.add_handler(CommandHandler('help', help))


def make_directory(update: Update, context: CallbackContext):
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
    # logic to change directories the terminal
    update.message.reply_text(
        "To change directories within the repository or directory you're in, "
        "use the `cd` command followed by the name of the directory you want "
        "to change to. For example if you want to move to 'my_directory' "
        "type the command:\n\n"
        "```\n"
        "cd my_directory\n"
        "```\n"
        "This will move you to the directory 'my_directory'\n"
        "To move out of your current directory and access the parent "
        "directory, use the command 'cd' followed by two dots(..) For "
        "instance if you want to access my_directory's parent directory use "
        "the following command:\n\n"
        "```\n"
        "cd ..\n"
        "```\n"
        "This will take you back a directory"
    )


updater.dispatcher.add_handler(CommandHandler(
    'change_directory', change_directory))


def list_files(update: Update, context: CallbackContext):
    # logic to list files in the terminal
    update.message.reply_text(
        "To list the files in your current directory, use the `ls` command. For example, run the following command in your terminal:\n\n"
        "```\n"
        "ls\n"
        "```\n"
        "This will list all the files in your current directory."
    )


updater.dispatcher.add_handler(CommandHandler('list_files', list_files))


def check_path(update: Update, context: CallbackContext):
    # logic to check the current path
    update.message.reply_text(
        "To check your current path, use the `pwd` command. For example, run the following command in your terminal:\n\n"
        "```\n"
        "pwd\n"
        "```\n"
        "This will display the current directory you're in."
    )


updater.dispatcher.add_handler(CommandHandler('check_path', check_path))


def print_file(update: Update, context: CallbackContext):
    # logic to print the contents of a file
    update.message.reply_text(
        "To print the contents of a file, use the `cat` command followed by the name of the file you want to print. For example, to print the contents of a file named 'example.txt', run the following command in your terminal:\n\n"
        "```\n"
        "cat example.txt\n"
        "```\n"
        "This will print the contents of the 'example.txt' file to your terminal."
    )


updater.dispatcher.add_handler(CommandHandler('print_file', print_file))


def display_txt(update: Update, context: CallbackContext):
    # logic to echo items on the terminal
    update.message.reply_text(
        "To display a line of text/string in the terminal use the 'echo' command. To use it, simply type the `echo` command followed by the text/string you want to display. For example:\n\n"
        "```\n"
        "echo 'Hello World!'\n"
        "```\n"
        "This will display the text 'Hello World!' in the terminal.")


updater.dispatcher.add_handler(CommandHandler('echo', display_txt))


def open_file(update: Update, context: CallbackContext):
    # logic to open file in vi
    update.message.reply_text(
        "To open a file in the terminal use the 'vi' command. To use it, simply type the `vi` command followed by the name of the file you want to open. For example:\n\n"
        "```\n"
        "vi myfile.txt\n"
        "```\n"
        "This will open the file `myfile.txt` in the terminal. You can then edit the contents of the file using the `vi` editor.\n\n"
        "To edit the contents of the file, press 'i' this will put you in insert mode and allow you to edit.\n\n"
        "To exit the file, press 'esc' then type ':wq' or ':x' or ':q!' depending on whether you want to save the contents of the file or exit without making changes\n")


updater.dispatcher.add_handler(CommandHandler('open_file', open_file))


def new_file(update: Update, context: CallbackContext):
    # logic to create a new file
    update.message.reply_text(
        "To create a new file in the terminal use the 'touch' command. To use it, simply type the `touch` command followed by the name of the file you want to create. For example:\n\n"
        "```\n"
        "touch myfile.txt\n"
        "```\n"
        "This will create a new file called `myfile.txt` in your current working directory.")


updater.dispatcher.add_handler(CommandHandler('new_file', new_file))


def delete_file(update: Update, context: CallbackContext):
    # logic to delete a file
    update.message.reply_text(
        "To delete a file in the terminal use the 'rm' command. To use it, simply type the `rm` command followed by the name of the file you want to delete. For example:\n\n"
        "```\n"
        "rm myfile.txt\n"
        "```\n"
        "This will delete the file called `myfile.txt` in your current working directory. Be careful with this command, as it permanently deletes the file and cannot be undone.")


updater.dispatcher.add_handler(CommandHandler('delete_file', delete_file))


def delete_dir(update: Update, context: CallbackContext):
    # logic to delete empty directory
    update.message.reply_text(
        "To delete an empty directory in the terminal use the 'rmdir' command. To use it, simply type the `rmdir` command followed by the name of the directory you want to delete. For example:\n\n"
        "```\n"
        "rmdir mydirectory\n"
        "```\n"
        "This will delete the empty directory called `mydirectory` in your current working directory. Note that this command can only delete empty directories, and not directories with files or subdirectories inside.")


updater.dispatcher.add_handler(CommandHandler('delete_directory', delete_dir))


def reply_to_text(update: Update, context: CallbackContext):

    # dictionary of text commands and their corresponding functions
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
    }

    # Handle normal text responses
    text = update.message.text.lower()

    try:
        commands[text](update, context)
    except KeyError:
        if text == "thank you":
            update.message.reply_text("You're welcome!")
        else:
            update.message.reply_text("Sorry, I didn't understand that.")


updater.dispatcher.add_handler(MessageHandler(Filters.text, reply_to_text))
updater.start_polling()
