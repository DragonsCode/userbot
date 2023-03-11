from config import *
from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
from pyrogram import filters, raw
import random

client = Client('ghoul-session', api_id, api_hash)

print('Бот запущен')


@client.on_message(filters.chat(1115897377))
def msg(client, message):
    pass
    #client.send_message(message.chat.id, "…"*random.randint(1,20))


@client.on_message(filters.regex("math") & filters.me)
def math(client, message):
    g=message.text.split()
    try:
        a=eval(g[1])
        message.edit_text(a)
    except SyntaxError and NameError:
        message.edit_text("Error")


@client.on_message(filters.regex("сердечко|Сердечко") & filters.me)
def serdce(client, message):
    #a="abcdefghijklmnopstuvwxyz"
    a="❤️🧡💛💚💙💜🖤🤍❤️🧡💛💚💙💜🖤🤍"
    for i in a:
        try:
            message.edit_text(i)
            sleep(0.5)
        except FloodWait as e:
            sleep(e.x)


@client.on_message(filters.chat(-1001316953070) & filters.regex('Тебе жаба, Милая Беседа ❤'))
def jaba(client, message):
    if message.from_user.id == 1124824021:
        client.send_message(message.chat.id, "Взять жабу")


@client.on_message(filters.regex('ping') & filters.me)
def ghoul_spam_handler(client, message):
    message.edit_text('pong')


@client.on_message(filters.regex('Я гуль|я гуль|Ghoul') & filters.me)
def ghoul_spam_handler(client, message):
    i = 1000
    while i > 0:
        try:
            client.send_message(message.chat.id, f'{i} - 7 = {i-7}')
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(1/messages_per_second)

    if(end_message == ''):
        client.send_message(message.chat.id, end_message)


@client.on_message(filters.command(ghoul_table_command, prefixes=command_prefixes) & filters.me)
def ghoul_table_handler(client, message):
    i = 1000
    while i > 62:
        try:
            text = f'{i} - 7 = {i-7}'
            for j in range(1,10):
                text += f'\n{i-7*j} - 7 = {i-7*(j+1)}'
            message.edit_text(f'`{text}`')
            sleep(sleep_time_ghoul)
        except FloodWait as e:
            sleep(e.x)

        i -= 7

    if(end_message != ''):
        client.send_message(message.chat.id, end_message)


@client.on_message(filters.regex("Красивоо" ) & filters.me)
def download_handler(client, message):
    message.reply_to_message.download()
    message.delete()


# @client.on_message()
# def online_handler(client, message):
#     client.send(raw.functions.account.UpdateStatus(offline=False))


client.run()