#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_file(update, context):
    update.message.reply_text(
        "To print the contents of a file, use the `cat` command followed by the name of the file you want to print. For example, to print the contents of a file named 'example.txt', run the following command in your terminal:\n\n"
        "```\n"
        "cat example.txt\n"
        "```\n"
        "This will print the contents of the 'example.txt' file to your terminal."
    )

def display_txt(update, context):
    update.message.reply_text(
        "To display a line of text/string in the terminal use the 'echo' command. To use it, simply type the `echo` command followed by the text/string you want to display. For example:\n\n"
        "```\n"
        "echo 'Hello World!'\n"
        "```\n"
        "This will display the text 'Hello World!' in the terminal."
    )

def open_file(update, context):
    update.message.reply_text(
        "To open a file in the terminal use the 'vi' command. To use it, simply type the `vi` command followed by the name of the file you want to open. For example:\n\n"
        "```\n"
        "vi myfile.txt\n"
        "```\n"
        "This will open the file `myfile.txt` in the terminal. You can then edit the contents of the file using the `vi` editor.\n\n"
        "To edit the contents of the file, press 'i' this will put you in insert mode and allow you to edit.\n\n"
        "To exit the file, press 'esc' then type ':wq' or ':x' or ':q!' depending on whether you want to save the contents of the file or exit without making changes\n"
    )

def new_file(update, context):
    update.message.reply_text(
        "To create a new file in the terminal use the 'touch' command. To use it, simply type the `touch` command followed by the name of the file you want to create. For example:\n\n"
        "```\n"
        "touch myfile.txt\n"
        "```\n"
        "This will create a new file called `myfile.txt` in your current working directory."
    )

def delete_file(update, context):
    update.message.reply_text(
        "To delete a file in the terminal use the 'rm' command. To use it, simply type the `rm` command followed by the name of the file you want to delete. For example:\n\n"
        "```\n"
        "rm myfile.txt\n"
        "```\n"
        "This will delete the file called `myfile.txt` in your current working directory. Be careful with this command, as it permanently deletes the file and cannot be undone."
    )
