#!/usr/bin/env python
# -*- coding: utf-8 -*-

def make_directory(update, context):
    update.message.reply_text(
        "To create a new directory, use the `mkdir` command followed by the name of the directory you want to create. For example, to create a directory called 'my_directory', you can run the following command in your terminal:\n\n"
        "```\n"
        "mkdir my_directory\n"
        "```\n"
        "This will create a new directory named 'my_directory' in your current working directory."
    )

def list_files(update, context):
    update.message.reply_text(
        "To list the files in your current directory, use the `ls` command. For example, run the following command in your terminal:\n\n"
        "```\n"
        "ls\n"
        "```\n"
        "This will list all the files in your current directory."
    )

def change_directory(update, context):
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
def delete_dir(update, context):
    update.message.reply_text(
        "To delete an empty directory in the terminal use the 'rmdir' command. To use it, simply type the `rmdir` command followed by the name of the directory you want to delete. For example:\n\n"
        "```\n"
        "rmdir mydirectory\n"
        "```\n"
        "This will delete the empty directory called `mydirectory` in your current working directory. Note that this command can only delete empty directories, and not directories with files or subdirectories inside."
    )

