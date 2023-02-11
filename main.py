# telebot это pyTelegramBotApi
# не путайте библиотеки 
# код может быть написан хуево но должен работать (с телефона не очень удобно кодить)
# тестовый бот (на котором тестился код - @xiaomiguys_bot - не обращайте внимания на его команды)
# код может быть нестабилен, нужны тесты
# переводы кривые (написаны вручную без переводчиков)
import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start']) #стартовая команда
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🇷🇺 Русский", callback_data="ru")
    btn2 = types.InlineKeyboardButton('🇬🇧 English', callback_data="en")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chatid = call.message.json["chat"]["id"] #колхоз для получения айди чата (правда бот по идее будет работать везде, даже не в лс)
    msgid = call.message.message_id
    if call.data == "ru":
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("Заскамиться", callback_data="scam")
            btn2= types.InlineKeyboardButton(text='Канал', url='https://t.me/lavkaton')
            btn3= types.InlineKeyboardButton(text='Сайт', url='https://lavkafoundation.fun')
            btn4= types.InlineKeyboardButton(text='Github', url='https://github.com/lavkacoin/autoscam')
            btn5 = types.InlineKeyboardButton('🔙 Вернуться к выбору языка', callback_data="languageswitch")
            markup.row(btn1)
            markup.row(btn2, btn3)
            markup.row(btn4)
            markup.row(btn5)
            bot.edit_message_text("Добро пожаловать в LAVKA autoscam. \n \n LAVKA autoscam - это открытая технология для скама. Если раньше вам приходилось покупать сомнительные NFT чтобы заскамиться, ждать скамеров - теперь вы можете просто нажать кнопку ниже. \n \n А так же можете посмотреть открытый исходный код этой технологии + подписаться на LAVKA Foundation.",chatid, msgid, parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup)
            try:            
                bot.answer_callback_query(call.id)
            except Exception as e:
            	print(f"шашыпка пофиг работаем дальше {e}")
    elif call.data == "en":
           markup = types.InlineKeyboardMarkup()
           btn1 = types.InlineKeyboardButton("Be scammed", callback_data="scam")
           btn2= types.InlineKeyboardButton(text='Channel', url='https://t.me/lavkaton')
           btn3= types.InlineKeyboardButton(text='Website', url='https://lavkafoundation.fun')
           btn4= types.InlineKeyboardButton(text='Github', url='https://github.com/lavkacoin/autoscam')
           btn5 = types.InlineKeyboardButton('🔙 Choose language', callback_data="languageswitch")
           markup.row(btn1)
           markup.row(btn2, btn3)
           markup.row(btn4)
           markup.row(btn5)
           bot.edit_message_text("Welcome to LAVKA autoscam. \n \n LAVKA autoscam - opened technology for scam. If you ever had to buy a questionable NFT to be scammed or wait for scammers - now you can simply press a button. \n \n Also you can watch the opened source code of this technology and subscribe to LAVKA Foundation.",chatid, msgid, parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup)
           try:            
                bot.answer_callback_query(call.id)
           except: 
            	print("шашыпка пофиг работаем дальше")
    elif call.data == "languageswitch":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("🇷🇺 Русский", callback_data="ru")
        btn2 = types.InlineKeyboardButton("🇬🇧 English", callback_data="en")
        markup.add(btn1, btn2)
        try:
            bot.edit_message_text("🇷🇺 Выберите язык / 🇬🇧 Choose your language", chatid, msgid, reply_markup=markup)        
            bot.answer_callback_query(call.id)
        except: 
            bot.send_message(chatid, "🇷🇺 Что-то пошло не так... попробуйте перезапустить бота - /start \n 🇬🇧 Something went wrong... Try to restart bot - /start")
    else:
        bot.send_message(chatid, "🇷🇺 Что-то пошло не так... попробуйте перезапустить бота - /start \n 🇬🇧 Something went wrong... Try to restart bot - /start")
        
bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть