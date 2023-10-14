#!/usr/bin/env python
# -*- coding: utf-8 -*-

def start(update, context):
    update.message.reply_text(
        "Hello there! Need help with the terminal?")

def help(update, context):
    update.message.reply_text(
        """
        **Linux Bot Commands:**

        /make_directory - Create a new directory
        /list_files - List files in your current directory
        /change_directory - Change your current directory
        /check_path - Check the current working directory
        /print_file - Print the contents of a file
        /display_txt - Display the contents of a file on the terminal
        /open_file - Open a file for editing
        /new_file - Create an empty file
        /delete_file - Delete a file in the terminal
        /delete_directory - Delete an empty directory
        /echo - Display text in the terminal
        /cat - Display the contents of a file
        /vi - Edit text files in the terminal
        /touch - Create a new file

        """
    )

