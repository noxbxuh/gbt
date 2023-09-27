from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
app_id = 15145595
app_hash = "c3f60ecf742e136436acc9082ac8d9a4"
session = os.environ.get("teleson")
StrPython = TelegramClient(StringSession(session), app_id, app_hash)
StrPython.start()
