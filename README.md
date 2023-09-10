# sending-messages-bot
Bot for sending messages to different users from database. Managed from another bot.

# Telegram Manager and Spam Bot Setup Guide

This guide will help you set up both a Telegram Manager and a Spam Bot using Python and the Telegram Bot API.

## Manager Bot Setup

### Step 1: Create a Manager Bot

1. Open Telegram and search for "@BotFather" or use this [link](https://t.me/BotFather) to open the BotFather chat.

2. Start a chat with BotFather and create a new bot by following the instructions. Once your bot is created, you will receive a token. Copy this token; you'll need it later.

### Step 2: Obtain API Credentials

1. Visit the [Telegram Apps page](https://my.telegram.org/auth?to=apps) and log in with your Telegram account.

2. Enter your phone number and follow the verification process to obtain your App `api_id` and `api_hash`. Also, provide an App title and a Short name.

### Step 3: Configure the .env File

1. Create a `.env` file in the root directory of your project.

2. Add the following lines to the `.env` file, replacing `<YOUR_TOKEN>`, `<YOUR_API_ID>`, and `<YOUR_API_HASH>` with the values you obtained in the previous steps:

3. Save the `.env` file.

## Spam Bot Setup

### Step 1: Switch to the Spam Bot Account

1. Log in to the Telegram account that you want to use for the Spam Bot.

### Step 2: Obtain API Credentials

1. Visit the [Telegram Apps page](https://my.telegram.org/auth?to=apps) and log in with your Telegram account.

2. Enter your phone number and follow the verification process to obtain your Spam Bot's App `api_id` and `api_hash`. Provide an App title and Short name as well.

### Step 3: Configure the .env File for Spam Bot

1. Open the `.env` file in the root directory of your project.

2. Modify the `.env` file to include the API credentials for the Spam Bot. Replace `<YOUR_TOKEN>`, `<YOUR_API_ID>`, and `<YOUR_API_HASH>` with the values obtained for the Spam Bot:

- `FROM` should be set to the username of your Manager Bot.

3. Save the `.env` file.

## Running the Bots

### Running the Manager Bot:

1. Open your terminal or command prompt.

2. Navigate to the root directory of your project.

3. Run the following command to start the Manager Bot:

```bash
py ./services/manager/manager.py
```
### Running the Spam Bot:

1. Open your terminal or command prompt.

2. Navigate to the root directory of your project.

3. Run the following command to start the Spam Bot:

```bash
py ./services/spambot/spam_bot.py
```
4. Enter the phone number associated with the Spam Bot account and complete the authentication process.
