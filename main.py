from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
from dotenv import load_dotenv
load_dotenv()

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_string = os.environ["SESSION_STRING"]

source_channel_id = 1002714330182
target_group_id = -1002840952584

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage(chats=[source_channel_id]))
async def handler(event):
    text = event.raw_text
    await client.send_message(target_group_id, text)

with client:
    client.run_until_disconnected()
