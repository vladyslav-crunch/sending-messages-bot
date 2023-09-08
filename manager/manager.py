from telethon.sync import TelegramClient
from telethon.tl import functions, types
from telethon import events, Button
from telethon.types import Message
import ast
from keyGen import keyGenerator
import config 
# Replace 'YOUR_API_KEY' with your actual Telegram Bot API key
client = TelegramClient('bot', config.MANAGER_APP_ID, config.MANAGER_API_HASH).start(bot_token=config.MANAGER_BOT_TOKEN)
# Start the client

client.parse_mode = 'HTML'
client.start()

# Dictionary to store user, message and database states
user_states = {}
message_states={}
user_database = {}

# Define the welcome message
welcome_message = "Добро пожаловать, этот бот создан для управления отправки сообщений по выбранной базе клиентов. По вопросам работы и пожеланиям обращайтесь к @nero_crunch и @Kubik0n"

# Start screen

@client.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    await event.respond(welcome_message, buttons=keyGenerator("start"))
    user_states[event.chat_id] = None
    user_database[event.chat_id] = None
   

# Main menu screen

@client.on(events.CallbackQuery(pattern=b'menu'))
async def callback(event):
    await event.respond("Вы находитесь в главном меню управления ботом. Пожалуйста выберите команду, которая вас интересует", buttons = keyGenerator("creating_database"))
    user_states[event.chat_id] = None
    user_database[event.chat_id] = None

# Creating message screen

@client.on(events.CallbackQuery(pattern=b'creating_message'))
async def callback(event):
    chat_id = event.chat_id
    await event.respond("Пожалуйста, напишите сообщение, которое хотите отправить", buttons = keyGenerator("menu"))
    user_states[chat_id] = "awaiting_input"

#user data base handler

@client.on(events.CallbackQuery(pattern=b'create_database'))
async def callback(event):
    chat_id = event.chat_id
    await event.respond("Пожалуйста, напишите юзернеймы пользователей, которым хотите отправить сообщение в формате: \n\ntom\nanna\nbob\n...", buttons = keyGenerator("menu"))
    user_states[chat_id] = "awaiting_database"

# Sending handler

@client.on(events.CallbackQuery(pattern=b'start_sending'))
async def callback(event):
    await client.edit_message(event.sender_id, event.message_id,'Рассылка началась! Подождите, пожалуйста.')
    current_message = message_states[event.chat_id]
    if current_message.grouped_id:
        text_html = repr(current_message.original_update.message.text + "SENDER_ID:" + str(event.chat_id) + 'TO_USERS="' + str(user_database[event.chat_id])+ '"').replace("\\n", "\r\n").replace("'","")
        await client.send_message(entity=config.SPAM_BOT_USERNAME,file=current_message.messages,parse_mode="HTML", message=text_html)
    else:
        text_html = repr(current_message.message.text + "SENDER_ID:" + str(event.chat_id)+ 'TO_USERS="' + str(user_database[event.chat_id])+ '"').replace("\\n", "\r\n").replace("'","")
        await client.send_message(entity = config.SPAM_BOT_USERNAME, message = text_html, parse_mode="html")
    message_states[event.chat_id] = None

# Message (text or image) handler

@client.on(events.NewMessage(func=lambda event: True))
async def handle_message(event):
    if not event.grouped_id:
        if event.chat_id in user_states:
            current_state = user_states[event.chat_id]
            if not event.is_private:
                return
            elif current_state == "awaiting_input":
                await client.send_message(entity=event.chat_id, message=event.message)
                await event.respond('Вы уверены, что хотите разослать именно это сообщение?', buttons=keyGenerator("confirming_message"))
                user_states[event.chat_id] = None
                message_states[event.chat_id] = event
            elif current_state == "awaiting_database":
                await client.send_message(entity=event.chat_id, message=event.message)
                await event.respond('Вы уверены, что хотите разослать сообщение именно этим пользователям?', buttons=keyGenerator("confirming_database"))
                user_states[event.chat_id] = None
                user_database[event.chat_id] = event.message.message

# Album handler

@client.on(events.Album(func=lambda event: True))
async def handle_message(event):
    if event.chat_id in user_states:
        current_state = user_states[event.chat_id]
        if not event.is_private:
            return
        if event.text == "":
            await event.respond("Пожалуйста, введите сообщение, которое вы хотите отправить.")
        elif current_state == "awaiting_input":
            text_html = repr(event.original_update.message.text).replace("\\n", "\r\n").replace("'","")
            await client.send_message(entity=event.chat_id,file=event.messages,parse_mode="HTML", message=text_html)
            await event.respond('Вы уверены, что хотите разослать именно это сообщение?', buttons=keyGenerator("confirming_message"))
            user_states[event.chat_id] = None
            message_data = event
            message_states[event.chat_id] = message_data



# Post sending callback handler

@client.on(events.NewMessage(from_users=[config.SPAM_BOT_USERNAME]))
async def handle_message(event):
    try:
        response = ast.literal_eval(event.message.message)
        message = (f'<i>Успешно отправлено</i> <b>{response["sent"]}</b> <i>пользователям,</i> 'f'<i>заблокировано</i> <b>{response["blocked"]}</b>')
        await client.send_message(entity=response["sender_id"], message=message ,parse_mode='html', buttons=keyGenerator("menu"))
    except Exception as e:
        print(e)

# None-stop bot working mode

with client:
    client.run_until_disconnected()


