import sys
sys.path.append('./cfg')
import config
import re

from telethon.sync import TelegramClient
from telethon import TelegramClient, events
from telethon.types import MessageMediaPhoto


def process_message(message):
    pattern = r'SENDER_ID:(\d+)TO_USERS=&quot;([^&]+)&quot;'
    match = re.search(pattern, message)
    sender_id = match.group(1)
    to_users = match.group(2)
    return {"sender_id": sender_id, "send_to": to_users} 

APP_ID = config.SPAM_BOT_APP_ID
API_HASH = config.SPAM_BOT_API_HASH
FROM = config.FROM


try:
    client = TelegramClient("session", api_id=APP_ID, api_hash=API_HASH)
    client.parse_mode = 'html'
    client.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

FROM = client.get_entity(FROM)

print("Starting...")
@client.on(events.NewMessage(from_users=FROM))
async def sender_bH(event):
    if isinstance(event.media, events.Album):
        recieved_message = repr(event.original_update.message.text).replace("\\n", "\r\n").replace("'","")
    else:
        recieved_message = repr(event.message.text).replace("\\n", "\r\n").replace("'","")
    message_to_send = recieved_message[:recieved_message.find("SENDER_ID:")]
    sent_counter = 0
    blocked_counter = 0
    users_to_send_list = [item.strip() for item in process_message(recieved_message)["send_to"].split('\n')]
    users_to_send = []
    for i in users_to_send_list:
        try:
            user_to_add = await client.get_entity(i)
            if user_to_add not in users_to_send:
                users_to_send.append()
        except Exception as e:
            blocked_counter+=1
            pass
    for i in users_to_send:
        try:
            if isinstance(event.media, events.Album):
                await client.send_message(entity=i,file=event.messages,parse_mode="HTML", message=message_to_send)
            elif isinstance(event.message.media, MessageMediaPhoto):
                await client.send_message(entity=i, file=event.message.media.photo, message=message_to_send, parse_mode="html")
            else:
                await client.send_message(entity = i, message = message_to_send, parse_mode="html")
            sent_counter+=1
        except Exception as e:
            print(e)
            blocked_counter+=1
            pass
    message_to_send = {"sent":sent_counter,"blocked":blocked_counter,"sender_id":int(process_message(recieved_message)["sender_id"])}
    await client.send_message(entity=event.chat_id, message=str(message_to_send))

client.run_until_disconnected()