import telebot

bot = telebot.TeleBot('6919907650:AAF2sCqJKqDlE1EpeG9bF3kk4FQ6eit4QFQ')

@bot.message_handler(commands=['start', 'hello', 'Привет'])
def main(message):
    bot.send_message(message.chat.id, f"Привет!  {message.from_user.first_name}")

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b>', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f"Привет!  {message.from_user.first_name}")
    elif message.text.lower() == 'id':
        bot.reply_to(message, f"ID: {message.from_user.id}")

bot.polling(none_stop=True)

