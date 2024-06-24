import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import logging

bot = Bot(token='7019735060:AAFSSQVQyLnEl1TMZ_TRS2djPuteaHaZ3ck')
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: Message):
    # Использование локального URL
    web_app_info = WebAppInfo(url='http://stark-frontend.vercel.app')
    button = KeyboardButton(text="Открыть веб страницу", web_app=web_app_info)
    
    # Создание клавиатуры и добавление кнопки
    markup = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)
    
    await message.answer("Привет!", reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
