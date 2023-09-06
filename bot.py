import telebot

# Replace 'YOUR_API_KEY' with your actual Telegram Bot API key
API_TOKEN = '6304262027:AAGEtu1B_E5JLKVtRdvkk8Ot9MFDtnAwuFo'

# Create an instance of the bot
bot = telebot.TeleBot(API_TOKEN)

# Define the welcome message
welcome_message = "Welcome to My Telegram Bot! Type /help to see available commands."

# Handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, welcome_message)

# Handler for all text messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "You said: " + message.text)

# Start the bot
bot.polling()
