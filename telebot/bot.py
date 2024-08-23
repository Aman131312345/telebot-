import telebot

# Укажите ваш токен бота
TOKEN = '7537412869:AAEpnGBLJk4bLqYK5L9K7AAhoA1Oiobmoyo'
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создание клавиатуры с кнопками
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('Armani')
    button2 = telebot.types.KeyboardButton('Video-Nike')
    button3 = telebot.types.KeyboardButton('Help')
    button4 = telebot.types.KeyboardButton('Audio') 
    button5 = telebot.types.KeyboardButton('Thank you')
    button6 = telebot.types.KeyboardButton('Bye')  
    keyboard.add(button1, button2, button3, button4,button5, button6)

    # Отправка приветственного сообщения с клавиатурой
    bot.send_message(message.chat.id, "Здраствуйте вас привестует официальный бот бренда Armani ", reply_markup=keyboard)

# Обработчик нажатия на кнопку "Nike"
@bot.message_handler(func=lambda message: message.text == 'Armani')
def send_nike(message):
    # Отправка изображения
    with open('image1.webp', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="Если вам нравится футболка тогда вы можете купить эту футболку за копейки нашем официальном сайте Armani")




@bot.message_handler(func=lambda message: message.text == 'Armani')
def send_nike(message):
    # Отправка изображения
    with open('image1.webp', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="This is the first shirt. Nice!")


# Обработчик нажатия на кнопку "Video-Nike"
@bot.message_handler(func=lambda message: message.text == 'Video-Armani')
def send_video_nike(message):
    # Отправка видео
    with open('NIKE - COMMERCIAL - 2024 -  JUST DO IT - AI ENTERTAINMENT.mp4', 'rb') as vid:
        bot.send_video(message.chat.id, vid, caption="Это видео.")

# Обработчик нажатия на кнопку "Help"
@bot.message_handler(func=lambda message: message.text == 'Help')
def send_help(message):
    # Отправка сообщения со справкой
    bot.send_message(message.chat.id, "Это справочное сообщение. Введите /start для начала работы с ботом.")

# Обработчик нажатия на кнопку "Audio"
@bot.message_handler(func=lambda message: message.text == 'Audio Armani')
def send_audio(message):
    # Отправка аудиосообщения
    with open('АДЛИН - No Love.mp3', 'rb') as audio:
        bot.send_voice(message.chat.id, audio, caption="Это аудиосообщение.")

        # Обработчик нажатия на кнопку "Audio"
@bot.message_handler(func=lambda message: message.text == 'Thank you')
def send_audio(message):
    # Отправка аудиосообщения
    with open('АДЛИН - No Love.mp3', 'rb') as audio:
        bot.send_voice(message.chat.id, audio, caption="No problem")


        # Обработчик нажатия на кнопку "Audio"
@bot.message_handler(func=lambda message: message.text == 'Bye ')
def send_audio(message):
    # Отправка аудиосообщения
    with open() as audio:
        bot.send_voice(message.chat.id, message, caption="Bye Bye")

# Запуск бота
bot.polling()