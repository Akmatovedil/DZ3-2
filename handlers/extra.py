import random

from aiogram import types, Dispatcher
from config import bot

async def echo(message: types.Message):
    bad = ['java', 'bitch', 'lox', 'kotlin', 'плохой мальчик']
    for word in bad:
        if word in message.text.replace(' ','').lower():
            await bot.send_message(message.chat.id, f'Не материтесь {message.from_user.full_name}')
            await bot.delete_message(message.chat.id, message.message_id)
    if message.text.startswith('!pin') and message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.message_id)
    if message.text.startswith('game'):
        arr = ['🎲', '😂', '🏆', '🧠' ]
        await bot.send_message(message.chat.id, random.choice(arr))

    # if message.text.lower() == 'dice':
    #     await bot.send_dice(message.chat.id, emoji=)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)

