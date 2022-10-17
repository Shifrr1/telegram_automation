# !/usr/bin/python3
# -*- coding: utf-8 -*-
import time
from telethon import TelegramClient, events

api_id = '<api_id>'  # Твой ID telegramm (https://core.telegram.org/api/obtaining_api_id)
api_hash = '<api_hash>'  # Твой api_hash Telegramm  (https://core.telegram.org/api/obtaining_api_id)
message = ''' Привет🖐'''
chat_to_check = 'chat_id=<id чата для проверки работы автоответчика>'
path_to = '<путь до сессии (Где она будет храниться)>'


def main():
    client = TelegramClient(f'{path_to}user_1', api_id, api_hash)
    client.start()
    mydict = []

    @client.on(events.NewMessage(incoming=True))  # @client.on(events.NewMessage(incoming=True))
    async def handler(event, mydict=mydict):

        print(time.asctime(), '-', event.message)
        full_data = ', '.join(mydict)
        sender = await event.get_sender()  # Нужен для проверки (sender.bot)
        if str(event.peer_id).find(chat_to_check) > 0:  # Чат для проверки работоспособности автоответчика
            await event.reply(message)
        if full_data.find(str(event.peer_id)) == -1 and str(event.peer_id).find('chat_id') == -1 and str(
                event.peer_id).find('channel_id') == -1 and not sender.bot:
            mydict.append(str(event.peer_id))
            await event.reply(message)

    print(time.asctime(), '-', 'Ожидание ...')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Остановка')


if __name__ == '__main__':
    main()
else:
    pass
