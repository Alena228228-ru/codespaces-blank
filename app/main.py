import telebot

token = '7500138759:AAHNhDCCjrt9ZRHSBWxIBHlmplNT4lyrS70'
bot = telebot.TeleBot(token, parse_mode = None)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
	bot.send_message(message.chat.id,"Привет")

# Вывод определенного сообщения при вводе опр.слова
@bot.message_handler(regexp = "kkk")
def  handle_message(message):
	bot.send_message(message.chat.id,"Привет")

@bot.message_handler(func=lambda message: True)
def test_callback(message): # <- passes a CallbackQuery type object to your function
    bot.send_message(message.chat.id, text='it`s test_callback')
# Копирование отправленного сообщения
#@bot.message_handler(func = lambda message: True)
#def echo_message(message):
#    bot.reply_to(message, message.text)

bot.infinity_polling()