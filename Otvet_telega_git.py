#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''Автоответчик подключается по вашому api_id и отвечает Юзерам телеграмма (не отвечает в каналы и чаты).
 Далее записывает ID в текстовый документ, для того чтобы не отправлять сообщение повторно тому же юзеру.
 При рестарте id.txt затирается'''
import time
from telethon import TelegramClient, events

try:
    from telethon import TelegramClient, eventsimport, connection
except ImportError:
		print("telethon module havn't been found. Use - pip3 install telethon")

api_id = '*********' #Твой ID telegramm (https://core.telegram.org/api/obtaining_api_id)
api_hash = '****************************' #Твой api_hash Telegramm  (https://core.telegram.org/api/obtaining_api_id)

message = ''' Привет🖐'''
def main():
    client = TelegramClient('user_1', api_id, api_hash)
    client.start()
    f = open('id.txt', 'w')
    f.close()
    @client.on(events.NewMessage(incoming= True))#    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        print(time.asctime(), '-', event.message)
        time.sleep(2)
        f = open('id.txt', 'r')
        id_list= []
        for i in f:
            id_list+=i.split()
        f.close()
        full_data = ', '.join(id_list)
        if str(event.peer_id).find('chat_id=********')>0: # Чат для проверки работоспособности автоответчика
            await event.reply(message)
        if full_data.find(str(event.peer_id))==-1 and str(event.peer_id).find('chat_id')==-1 and str(event.peer_id).find('channel_id')==-1:
            with open(file='id.txt', mode='a', encoding='utf-8') as file:
                file.write(f'\n{event.peer_id}')
            await event.reply(message)


    print(time.asctime(), '-', 'Waiting for incoming messages...')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')


if __name__ == '__main__':
    main()
else:
    pass
 # https://docs.python.org/2/library/os.html