import  telebot
import constant
import time
import  datetime

bot = telebot.TeleBot(constant.token)

upd = bot.get_updates()
#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)



print(bot.get_me())

def log (message,answer):
    print("\n~~~~~")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1} - id = {2} \n Текст  = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)




@bot.message_handler(commands=["help"])
def handle_text(message):
    bot.send_message(message.chat.id, "Чем я могу тебе помочь - выбери вариант 1 или 2")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, constant.first_mess)

user_select = constant.INIT_WEB;

last_message = ""
@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = "Люблю тебя сильно"

    if message.text == constant.FIRST_WEB:
        answer = constant.second_ok
        user_select = constant.FIRST_WEB
    elif message.text == constant.SECONT_WEB:
        answer = constant.second_ok
        user_select = constant.SECONT_WEB
    #else:
        #answer = constant.SELECT_WEB
    log(message, answer)
    last_message = answer
    bot.send_message(message.chat.id, answer)
    if (user_select == constant.FIRST_WEB) or (user_select == constant.SECONT_WEB):
        time.sleep(10)
        bot.send_message(message.chat.id, constant.second_ok2)


@bot.message_handler(func=lambda message: False) #cause there is no message
def first_web_message():
    now = datetime.now()
    if now.time() == time(18,25):
        bot.send_message(message.chat.id, constant.WEB_1h)
    if (user_select == constant.FIRST_WEB)  and (now.date().weekday() == 4) and (now.time() == time(18,23)):
        bot.send_message(message.chat.id, constant.WEB_1h)
    if (user_select == constant.FIRST_WEB)  and (now.date().weekday() == 2) and (now.time() == time(12,55)):
        bot.send_message(message.chat.id, constant.WEB_5m)
    if (user_select == constant.FIRST_WEB)  and (now.date().weekday() == 2) and (now.time() == time(14,15)):
        bot.send_message(message.chat.id, constant.READY)


bot.polling(none_stop=True, interval=0)