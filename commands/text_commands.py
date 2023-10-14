#!/usr/bin/env python
# -*- coding: utf-8 -*-

def echo(update, context):
    update.message.reply_text(
        "The `echo` command in Linux is used to display text in the terminal. "
        "You can use it to print messages or variables. For example:\n\n"
        "```\n"
        "$ echo 'Hello, World!'\n"
        "Hello, World!\n"
        "```\n"
        "You can also use variables within the text. For instance:\n\n"
        "```\n"
        '$ echo "Today is $(date)"\n'
        "Today is Wed Jan 1 12:00:00 UTC 2023\n"
        "```\n"
        "The `echo` command is commonly used in shell scripts and for printing messages to the terminal."
    )

def cat(update, context):
    update.message.reply_text(
        "The `cat` command in Linux is used to display the contents of a file. "
        "For example:\n\n"
        "```\n"
        "$ cat file.txt\n"
        "Hello, World!\n"
        "```\n"
        "You can also use it to display multiple files at once. For instance:\n\n"
        "```\n"
        "$ cat file1.txt file2.txt\n"
        "Hello, World!\n"
        "Hello, World!\n"
        "```\n"
        "The `cat` command is commonly used in shell scripts and for printing messages to the terminal."
    )

def vi(update, context):
    update.message.reply_text(
        "The `vi` command in Linux is used to edit text files. "
        "It can be used to create new files, edit existing ones, or view their contents. "
        "For example:\n\n"
        "```\n"
        "$ vi file.txt\n"
        "```\n"
        "This will open the file in the `vi` editor. "
        "You can then use the arrow keys to move around the file, "
        "and the `i` key to enter insert mode. "
        "Once you are done editing the file, press `Esc` to exit insert mode, "
        "and then type `:wq` to save and quit the editor."
    )

def touch(update, context):
    update.message.reply_text(
        "The `touch` command in Linux is used to create new files. "
        "For example:\n\n"
        "```\n"
        "$ touch file.txt\n"
        "```\n"
        "This will create a new file called `file.txt` in the current directory."
    )


