import telebot
from telebot import types

bot = telebot.TeleBot('6919907650:AAF2sCqJKqDlE1EpeG9bF3kk4FQ6eit4QFQ')


@bot.message_handler(commands=['start', 'hello', 'привет'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Deleted')




@bot.message_handler()
def get_photo(message):
    if message.text.lower() == 'инстаграмм Бекастана' or 'site' or 'site bekastan':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.instagram.com/5ekastan')
        btn2 = types.InlineKeyboardButton('Удалить текст', callback_data='delete')
        btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
        markup.row(btn1)
        markup.row(btn2, btn3)
        bot.reply_to(message, "Это сайт Бекастана", reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.message_id)
bot.polling(none_stop=True)
