import telegram

def MyTelegram():

    bot = telegram.Bot(token='1751413623:AAGqoVnH_9OE9sccrNOi1ozES27uWb-xhD0')
    chat_id = 1878240999

    bot.sendMessage(chat_id=chat_id, text='텔레그램 실험')