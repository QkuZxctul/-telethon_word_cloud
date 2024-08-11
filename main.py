from asyncio import run
from os import remove

from src.utils.telethon_functions import dump_messages
from src.utils.make_cloud import cloud
from src.utils.loader import client

if __name__ == '__main__':
    chat = 'clouds' + input('Введите юз диалога для создания облака слов: ')
    run(dump_messages(client, chat))
    with open(chat + '.txt', 'r', encoding='UTF-8') as f:
        text = f.readlines()
        text = ' '.join(text)
        cloud(text, chat)
    remove(chat + '.txt')