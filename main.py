import telebot
from telebot import types
from PIL import Image , ImageDraw, ImageFont
import re

hideBoard = types.ReplyKeyboardRemove()

token = '******************'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_def(message):
    if str(message.from_user.id) == "397448482" or str(message.from_user.id) == "891705090":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сделать скрин авиатора")
        markup.add(btn1)
        send1 = bot.send_message(message.from_user.id, "Выберите команду", reply_markup=markup)
        bot.register_next_step_handler(send1, screen_prov)

@bot.message_handler(commands=["screen"])
def screen_prov(message):
    if str(message.from_user.id) == "397448482" or str(message.from_user.id) == "891705090":
        if message.text == "/screen" or message.text == "Сделать скрин авиатора" :
            send1 = bot.send_message(message.from_user.id, "Напишите параметры в виде:  10:41:44 4000 3.54 10:44:13 7000 8.32", reply_markup=hideBoard)
            bot.register_next_step_handler(send1, screen_def)
        else:
            bot.send_message(message.from_user.id, "Что то пошло не так, попробуйте заново")
            start_def(message)


def screen_def(message):
 try:
    text1 = message.text.split()
    time1 = text1[0]
    time2 = text1[3]
    bet1 = re.sub(r"\B(?=(?:\d{3})+,)", " ", text1[1]+",00")
    bet2 = re.sub(r"\B(?=(?:\d{3})+,)", " ", text1[4] + ",00")
    kef1 = text1[2]
    kef2 = text1[5]
    win1 = re.sub(r"\B(?=(?:\d{3})+,)", " ", str(float(text1[2])*float(text1[1])).split(".")[0]+",00")
    win2 = re.sub(r"\B(?=(?:\d{3})+,)", " ", str(float(text1[5])*float(text1[4])).split(".")[0]+",00")
    sample = Image.open('13.jpg')
    pencil = ImageDraw.Draw(sample)

    font = ImageFont.truetype('C:/Users/Тимур/PycharmProjects/pythonProject1/aviator/Manrope-Medium.ttf', size=33)
    font2 = ImageFont.truetype('C:/Users/Тимур/PycharmProjects/pythonProject1/aviator/Manrope-Medium.ttf', size=26)
    font3 = ImageFont.truetype('C:/Users/Тимур/PycharmProjects/pythonProject1/aviator/Manrope-Medium.ttf', size=28)
    #Время
    pencil.text((77, 215), time1, font=font, fill="#948ac5")
    pencil.text((77, 340), time2, font=font, fill="#948ac5")
    #Ставка
    if len(text1[1])<5:
        pencil.text((295, 218), bet1, font=font2)
    else:
        pencil.text((280, 218), bet1, font=font2)
    if len(text1[4])<5:
        pencil.text((295, 344), bet2, font=font2)
    else:
        pencil.text((280, 344), bet2, font=font2)


    #выигрыш
    if len(win1)<10:
        pencil.text((655, 218), str(win1), font=font2)
    elif len(win1)<11:
        pencil.text((630, 218), str(win1), font=font2)
    elif len(win1)<12:
        pencil.text((615, 218), str(win1), font=font2)
    elif len(win1)<13:
        pencil.text((600, 218), str(win1), font=font2)


    if len(win2)<10:
        pencil.text((655, 344), str(win2), font=font2)
    elif len(win2)<11:
        pencil.text((630, 344), str(win2), font=font2)
    elif len(win2)<12:
        pencil.text((615, 344), str(win2), font=font2)
    elif len(win2)<13:
        pencil.text((600, 344), str(win2), font=font2)


    if float(kef1)<2:
        pencil.rounded_rectangle((470, 202, 615, 268), fill="#3e5bc1", width=3, radius=15)
    elif float(kef1)<10:
        pencil.rounded_rectangle((470, 202, 615, 268), fill="#773dbc", width=3, radius=15)
    else:
        pencil.rounded_rectangle((470, 202, 615, 268), fill="#e89106", width=3, radius=15)

    if float(kef2)<2:
        pencil.rounded_rectangle((470, 328, 615, 394), fill="#3e5bc1", width=3, radius=15)
    elif float(kef2)<10:
        pencil.rounded_rectangle((470, 328, 615, 394), fill="#773dbc", width=3, radius=15)
    else:
        pencil.rounded_rectangle((470, 328, 615, 394), fill="#e89106", width=3, radius=15)

    if len(kef1)<2:
        pencil.text((527, 218), kef1+"x", font=font3)
    elif len(kef1)<4:
        pencil.text((517, 218), kef1+"x", font=font3)
    elif len(kef1)<5:
        pencil.text((508, 218), kef1+"x", font=font3)
    else:
        pencil.text((505, 218), kef1+"x", font=font3)

    if len(kef2)<2:
        pencil.text((527, 344), kef2 + "x", font=font3)
    elif len(kef2)<4:
        pencil.text((517, 344), kef2+"x", font=font3)
    elif len(kef2)<5:
        pencil.text((508, 344), kef2 + "x", font=font3)
    else:
        pencil.text((505, 344), kef2 + "x", font=font3)
    bot.send_photo(message.from_user.id, sample)

 except:
     bot.send_message(message.from_user.id,"Что то пошло не так, попробуйте заново")
     start_def(message)

if 1:
    bot.infinity_polling(skip_pending=True)
