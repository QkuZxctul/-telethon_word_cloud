from telethon import TelegramClient
from telethon.errors import *

async def dump_messages(client: TelegramClient, chat):
    try:  
        await client.start()
        async with client.takeout() as takeout:  
            filename = f'clouds/{chat}.txt'
            with open(filename, 'w', encoding='UTF-8') as file:
                async for message in takeout.iter_messages(chat, wait_time=0):
                    try:
                        file.write(str(message.message) + '\n')
                    except Exception as ex:
                        continue
            return filename
        
    except TakeoutInitDelayError as e:  
        print('Must wait', e.seconds, 'before takeout')
        