from telethon import TelegramClient
from backend.config import API_ID, API_HASH, TG_DEVICE_MODEL, TG_APP_VERSION, TG_SYSTEM_VERSION, TG_LANG_CODE
import uuid
import os

os.makedirs("sessions", exist_ok=True)


def create_client(device_model: str | None = None,
                  app_version: str | None = None,
                  system_version: str | None = None,
                  lang_code: str | None = None):
    """Create a Telethon TelegramClient with optional customization of
    device/app/system strings that Telegram shows in Active Sessions.

    You can set defaults via environment (.env) using the variables
    TG_DEVICE_MODEL, TG_APP_VERSION, TG_SYSTEM_VERSION, TG_LANG_CODE.
    """
    session = f"sessions/{uuid.uuid4().hex}"

    # fall back to configured defaults
    device_model = device_model or TG_DEVICE_MODEL
    app_version = app_version or TG_APP_VERSION
    system_version = system_version or TG_SYSTEM_VERSION
    lang_code = lang_code or TG_LANG_CODE

    client = TelegramClient(
        session,
        API_ID,
        API_HASH,
        device_model=device_model,
        system_version=system_version,
        app_version=app_version,
        lang_code=lang_code,
    )

    # best-effort record of session path for LoginState.create
    try:
        client._session_path = session
    except Exception:
        pass

    return client
