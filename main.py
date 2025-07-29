import os
from telethon import TelegramClient, events
from dotenv import load_dotenv
import requests

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://your-n8n-webhook-url")

# Создание клиента
client = TelegramClient("dnk_session", API_ID, API_HASH)

# Список каналов для мониторинга (можно использовать username или ID)
TARGET_CHANNELS = [
    "radnykukr", "kpszsu", "spravdi", "kiev_pravyy_bereg", "TCH_channel",
    "UaOnlii", "insiderUKR", "censor_net", "dsns_telegram",
    "KyivCityOfficial", "UA_National_Police", "truexakhersonua", "kiev_svet"
]

KEYWORDS = [
    "тривога", "удар", "ракета", "ППО", "дрон", "Shahed", "вибух", "запуск",
    "Іскандер", "прильот", "обстріл", "загроза"
]

@client.on(events.NewMessage)
async def handler(event):
    if not event.message.message:
        return

    sender = await event.get_chat()
    sender_username = getattr(sender, 'username', None)

    if sender_username not in TARGET_CHANNELS:
        return

    text = event.message.message.lower()
    if any(k in text for k in KEYWORDS):
        print(f"[MATCH] From @{sender_username}: {event.message.message[:60]}...")
        try:
            requests.post(WEBHOOK_URL, json={
                "channel": sender_username,
                "message": event.message.message
            })
        except Exception as e:
            print(f"Webhook error: {e}")

client.start()
print("✅ DNK userbot is running...")
client.run_until_disconnected()
