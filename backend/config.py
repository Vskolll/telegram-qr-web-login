import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("TG_API_ID"))
API_HASH = os.getenv("TG_API_HASH")
# Optional fields to customize how the Telegram session appears in
# Active Sessions / Devices. Set these in your .env if you want a
# custom device/app name to show up (e.g. "Esports pubg mobile Login").
TG_DEVICE_MODEL = os.getenv("TG_DEVICE_MODEL", "Esports pubg mobile Login")
TG_APP_VERSION = os.getenv("TG_APP_VERSION", "1.42.0")
TG_SYSTEM_VERSION = os.getenv("TG_SYSTEM_VERSION", "Android 25.0.0")
TG_LANG_CODE = os.getenv("TG_LANG_CODE", "ru")
