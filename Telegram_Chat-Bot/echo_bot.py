import telebot
from config import bot


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <strong>{message.from_user.first_name} {message.from_user.last_name}</strong>! How its going?\
            \nIam a bot, that will help u to fast search information about mixed drinks from all over the world!\
            \nJust enter the cocktail name and i will give all information i have'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_message(message):
    if message.text == 'daiquiri' or message.text == 'Daiquiri' or message.text == 'дайкири' or message.text == 'Дайкири':
        recipe = f'bla\nbla'
        bot.send_message(message.chat.id, recipe, parse_mode='html')
    elif message.text != 'daiquiri':
        bot.send_message(message.from_user.id, "Напиши привет")
    # bot.send_message(message.chat.id, message, parse_mode='html')


#That will start a bot
bot.polling(none_stop = True)