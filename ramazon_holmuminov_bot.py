import telebot

bot = telebot.TeleBot('2059791236:AAHjx2lIDBhYPbH9ItFq_27DDeplKG67Pa4')


@bot.message_handler(commands=['start'])
def start(message):
    name = str(message.from_user.first_name)
    bot.send_message(message.from_user.id, 'Assalom aleykum ' + name)
    # bu yerda user /start bosganda Isminmi olib Salom qowb yuboradi
    # message bu json telegram server bizga xabarda json api yuboradi uni ichida userga tegishli #barcha narsa bor


@bot.message_handler(content_types=['text'])
def send(message):
    text = message.text
    if text == 'Python':
        bot.send_message(message.from_user.id, 'Salom Python Programist')
    elif text == 'Java':
        bot.send_message(message.from_user.id, 'Salom Java Programist')
    elif text == 'Php':
        bot.send_message(message.from_user.id, 'Salom Php Programist')
    elif text == 'C#':
        bot.send_message(message.from_user.id, 'Salom C# Programist')
    else:
        bot.send_message(message.from_user.id, 'Uzur men sizi tanimayaman 😑😂')


bot.polling(none_stop=True)  # bu botimiz o'chib qolmasligi uchun!
