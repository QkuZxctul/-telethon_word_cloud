from dotenv import load_dotenv
from os import getenv

from telethon import TelegramClient

load_dotenv('.env')

API_ID = getenv('api_id')
API_HASH = getenv('api_hash')

assert API_ID and API_HASH

client = TelegramClient('.session', api_hash=API_HASH, api_id=API_ID, system_version="4.16.30-vxqwerty")
