from telethon import TelegramClient, events
from telethon.tl.types import MessageEntityCustomEmoji, MessageEntityTextUrl

api_id = 28774428
api_hash = 'a21dbda93eaa482f8fc5400eec247cbf'
session_name = 'main'

source_channel_id = 1002707233772
TARGET_CHAT_ID = -1002725548194

EMOJI_ID = 5204394597651871345
LINK = "https://t.me/dnk_news"
TEXT = "ДНК * Україна 👈 Підписатися"

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL_ID))
async def handler(event):
    try:
        message = event.message
        await client.send_message(TARGET_CHAT_ID, message, file=message.media)
        await client.send_message(
            TARGET_CHAT_ID,
            TEXT,
            entities=[
                MessageEntityCustomEmoji(offset=4, length=1, document_id=EMOJI_ID),
                MessageEntityTextUrl(offset=0, length=len(TEXT), url=LINK)
            ]
        )
    except Exception as e:
        print(f"❌ Ошибка: {e}")

client.start()
print("✅ Бот запущен.")
client.run_until_disconnected()
