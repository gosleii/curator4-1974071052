import telebot
bot = telebot.TeleBot("7436184519:AAGlmevNWX0iW3A4cVKwrhfdJjXJsqAn5JM")

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Добро пожаловать в наш магазин! Подсказать Вам что-нибудь?")

@bot.message_handler(commands=["choice"])
def choice_handler(message):
    bot.send_message(message.chat.id, "У нас Вы можете найти *хлеб*, *молоко* и *шоколад*", parse_mode="Markdown")

@bot.message_handler(commands=["buy"])
def buy_handler(message):
    bot.send_message(message.chat.id, "Отлично! _С Вас 2 монетки._ До свидания, хорошего дня!", parse_mode="Markdown")

@bot.message_handler(commands=["not_found"])
def not_found_handler(message):
    bot.send_message(message.chat.id, "Не нашли чего-то из продуктов? Загляните [сюда!](https://samokat.ru/)", parse_mode="Markdown")

bot.infinity_polling()