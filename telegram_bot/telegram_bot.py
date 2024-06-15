import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


class TelegramBot:
    def __init__(self, token, chat_id=None):
        self.token = token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{self.token}/"

    def send_message(self, text):
        url = self.base_url + "sendMessage"
        payload = {
            'chat_id': self.chat_id,
            'text': text
        }
        response = requests.post(url, data=payload)
        return response.json()

    def get_updates(self, offset=None, timeout=3):
        url = self.base_url + "getUpdates"
        payload = {
            'timeout': timeout,
            'offset': offset
        }
        response = requests.get(url, params=payload)
        return response.json()


def send_message(text):
    zzabis = TelegramBot(TOKEN, CHAT_ID)
    zzabis.send_message(text)
