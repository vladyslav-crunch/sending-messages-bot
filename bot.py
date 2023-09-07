from telethon.sync import TelegramClient
from telethon.tl import functions, types
from telethon import events, Button
# Replace 'YOUR_API_KEY' with your actual Telegram Bot API key
client = TelegramClient('bot', 26560112, 'f0bb00853bfd5a2d250f8182d3466703').start(bot_token='6304262027:AAGEtu1B_E5JLKVtRdvkk8Ot9MFDtnAwuFo')
# Start the client
client.start()


# Dictionary to store user states
user_states = {}






# Define the welcome message
welcome_message = "Добро пожаловать, этот бот создан для управления отправки сообщений по выбранной базе клиентов. По вопросам работы и пожеланиям обращайтесь к @nero_crunch и @Kubik0n"
creating_message_message = "Напишите сообщение, которое хотите отправить"


@client.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    await event.respond('Добро пожаловать, этот бот создан для управления отправки сообщений по выбранной базе клиентов. По вопросам работы и пожеланиям обращайтесь к @nero_crunch и @Kubik0n', buttons=[
        [Button.inline("Написать сообщение", b"creating_message")]
    ])

@client.on(events.CallbackQuery(pattern=b'creating_message'))
async def callback(event):
    chat_id = event.chat_id
    await event.respond("Напишите сообщение, которое хотите отправить")
    user_states[chat_id] = "awaiting_input"


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
            user_states[event.chat_id] = None
# Start the TelegramClient

# @client.on(events.NewMessage(func=lambda event: True))
# async def handle_message(event):
#     if not event.is_private:
#         return
    
#     else:
#         await client.send_message(entity=event.chat_id, message=event.message)

with client:
    client.run_until_disconnected()









# @client.on(events.NewMessage)
# async def handle_new_message(event):
#     chat_id = event.chat_id
#     message_text = event.raw_text

#     if chat_id in user_states:
#         current_state = user_states[chat_id]

#         # Implement your conversation logic based on the current state
#         if current_state == "awaiting_input":
#             await event.reply(f"You entered: {message_text}")
#             # Reset the user state after handling the input
#             user_states[chat_id] = None
#         else:
#             await event.reply("Please start a conversation.")

#     elif message_text.lower() == "/start":
#         await event.reply("Welcome! Please enter something:")
#         # Set the user state to "awaiting_input" to track the conversation flow
#         user_states[chat_id] = "awaiting_input"
#     else:
#         await event.reply("Please start a conversation by sending /start.")


# Run the client to listen for events
