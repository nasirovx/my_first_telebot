import telebot
import requests
import json
import os

bot = telebot.TeleBot('6919907650:AAF2sCqJKqDlE1EpeG9bF3kk4FQ6eit4QFQ')
API = '729186aee2ec1a6d1b3d520bc1751e81'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')

script_dir = os.path.dirname(os.path.abspath(__file__))

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}')
    if res.status_code == 200:
        data = res.json()
        temp_kelvin = data['main']['temp'] 
        temp_celsius = temp_kelvin - 273.15  
        bot.reply_to(message, f'Сейчас погода: {temp_celsius:.2f} градусов по Цельсию')

        image = 'summer.png' if temp_celsius > 5.0 else 'ob.jpg'
        file_path = os.path.join(script_dir, image)
        with open(file_path, 'rb') as file:
            bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, "Город указан не верно!")


bot.polling(none_stop=True)
