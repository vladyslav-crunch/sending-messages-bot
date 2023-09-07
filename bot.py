from telethon.sync import TelegramClient
from telethon.tl import functions, types
from telethon import events, Button
from telethon.types import Message
# Replace 'YOUR_API_KEY' with your actual Telegram Bot API key
client = TelegramClient('bot', 26560112, 'f0bb00853bfd5a2d250f8182d3466703').start(bot_token='6304262027:AAGEtu1B_E5JLKVtRdvkk8Ot9MFDtnAwuFo')
# Start the client
client.start()


# Dictionary to store user states
user_states = {}
message_states={}


# Define the welcome message
welcome_message = "Добро пожаловать, этот бот создан для управления отправки сообщений по выбранной базе клиентов. По вопросам работы и пожеланиям обращайтесь к @nero_crunch и @Kubik0n"
creating_message_message = "Напишите сообщение, которое хотите отправить"

#Стартовий Екран

@client.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    await event.respond(welcome_message, buttons=[
        [Button.inline("В меню", b"menu")]
    ])

#Екран меню

@client.on(events.CallbackQuery(pattern=b'menu'))
async def callback(event):
    chat_id = event.chat_id
    await event.respond("Вы находитесь в главном меню управления ботом. Пожалуйста выберите команду, которая вас интересует", buttons = [Button.inline("Создать сообщения для рассылки", b"creating_message")])
    user_states[chat_id] = "awaiting_input"

#Екран создания сообщения 

@client.on(events.CallbackQuery(pattern=b'creating_message'))
async def callback(event):
    chat_id = event.chat_id
    await event.respond("Пожалуйста, напишите сообщение, которое хотите отправить", buttons = [Button.inline("Назад в меню", b"menu")])
    user_states[chat_id] = "awaiting_input"

#Обработка россылки

@client.on(events.CallbackQuery(pattern=b'start_sending'))
async def callback(event):
    await client.edit_message(event.sender_id, event.message_id,'Начало россылки...')
    current_message = message_states[event.chat_id]
    if isinstance(current_message, Message):
        await client.send_message(entity=404465503, message=current_message)
    else:
        await client.send_message(entity=404465503, file=current_message[0], message = current_message[1])
        
    message_states[event.chat_id] = None

#Обработчик текста и картинок

@client.on(events.NewMessage(func=lambda event: True))
async def handle_message(event):
    if not event.grouped_id:
        if event.chat_id in user_states:
            current_state = user_states[event.chat_id]
            if not event.is_private:
                return
            elif current_state == "awaiting_input":
                await client.send_message(entity=event.chat_id, message=event.message)
                await event.respond('Вы уверены, что хотите разослать именно это сообщение?', buttons=[
                [Button.inline("Да, я уверен (начать рассылку)", b"start_sending")],[Button.inline("Нет, я ошибся", b"creating_message")]
                ])
                user_states[event.chat_id] = None
                message_states[event.chat_id] = event.message
                print("I get an text")

#Обработчик альбомов 

@client.on(events.Album(func=lambda event: True))
async def handle_message(event):
    if event.chat_id in user_states:
        current_state = user_states[event.chat_id]
        if not event.is_private:
            return
        if event.text == "":
            await event.respond("Пожалуйста, введите сообщение, которое вы хотите отправить.")
        elif current_state == "awaiting_input":
            await client.send_message(entity=event.chat_id,file=event.messages, message=event.original_update.message.message)
            await event.respond('Вы уверены, что хотите разослать именно это сообщение?', buttons=[
            [Button.inline("Да, я уверен (начать рассылку)", b"start_sending")],[Button.inline("Нет, я ошибся", b"creating_message")]
            ])
            user_states[event.chat_id] = None
            message_data = (event.messages, event.original_update.message.message)
            message_states[event.chat_id] = message_data
            print("I get an album")

#Обработка начала россилки

@client.on(events.NewMessage(func=lambda event: True))
async def handle_message(event):
    if not event.grouped_id:
        if event.chat_id in user_states:
            current_state = user_states[event.chat_id]
            if not event.is_private:
                return
            elif current_state == "awaiting_input":
                await client.send_message(entity=event.chat_id, message=event.message)
                await event.respond('Вы уверены, что хотите разослать именно это сообщение?', buttons=[
                [Button.inline("Да, я уверен (начать рассылку)", b"start_sending")],[Button.inline("Нет, я ошибся", b"creating_message")]
                ])
                user_states[event.chat_id] = None
                message_states[event.chat_id] = event.message
                print("I get an text")

   
with client:
    client.run_until_disconnected()


