# Commandline_Guru

Commandline_Guru is a Telegram bot designed to provide useful command-line tips and tricks to users. It aims to help users improve their productivity and efficiency when working on the command line.

## Features

Some of the key features of Commandline_Guru include:

- Providing tips and tricks for working on the command line, including useful commands and keyboard shortcuts
- Allowing users to search for specific tips using keywords or phrases
- Providing random tips and tricks for users who want to learn something new
- Allowing users to save their favorite tips for later reference
- Providing a friendly, conversational interface that makes learning about the command line more engaging and enjoyable

## Technologies Used

Commandline_Guru was built using the following technologies:

- Python 3
- Telepot library for building Telegram bots

## Usage


To use this program, you will need to have Python 3 installed on your computer.

### Cloning The Repository

To clone the repository, open a terminal and run the following command:

> git clone https://github.com/chriss1525/Commandline_Guru.git

### Installing Dependencies

Once you have cloned the repository, navigate to the project directory and install the necessary dependencies by running:

> pip install python-telegram-bot

### Running the Program

To run the program, navigate to the project directory in your terminal and run the following command:

> python commandline_guru.py

### Setting Up Your Telegram Bot

To use this program with your own Telegram Bot, you will need to create a bot account and obtain a bot token. Here's how to do it:

- Open Telegram and search for the @BotFather bot.

- Start a chat with @BotFather and send the command /newbot.

- Follow the instructions to provide a name and username for your bot.

- Once you have created the bot, @BotFather will give you a bot token. Make sure to copy and save it in a secure place.

- Create a .env file and store your bot token as Token='your_bot_token_here'

- Configure your bot's settings in the Telegram Bot API as desired.

That's it! Once you have obtained your bot token and configured your bot in the Telegram Bot API, you can run the program and start interacting with your bot.


If you keep the current configurations of the bot, open a chat with the bot @commandline_guru_bot and type any of the following commands:

- /make_directory - how to create a new directory
- /list_files: how to list files in your currenct directory
- /change_directory: how to change your current directory
- /check_path: how to check the path you are currently in
- /print_file: how to print the contents of a file
- /display_txt: how to display the contents of a file on the terminal
- /open_file: how to open a file on the terminal for editing purposes
- /new_file: how to create an empty file
- /delete_file: how to delete a file in the terminal
- /delete_directory: how to delete an empty directory

### Future Work


In the future, I plan to add the following features to Commandline_Guru:

- Support for multiple languages, so users can receive tips in their preferred language
- Integration with external APIs and services to provide even more helpful tips and tricks
- Support for sharing tips and tricks with other users and on social media platforms


### Contributors
This project was developed by [Christine Okoth](https://github.com/Chriss1525), with contributions from [Akuya Ekorot](https://github.com/akuya-ekorot).

License
Commandline_Guru is released under the MIT License.
