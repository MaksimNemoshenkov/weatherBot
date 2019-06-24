import telebot
import pyowm

owm = pyowm.OWM('1a6ea18e4e93092900decd096348d891', language="ua")
bot = telebot.TeleBot("820398697:AAHYw96gG1jXraJQr3bNWEb2-Ew8QlRLkXE")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    bot.send_message(message.chat.id, message.text)
    temp = w.get_temperature('celsius')["temp"]

    answer = ("В місті " + message.text + " " + w.get_detailed_status() + "\n")
    answer += ("Tемпература зараз " + str(temp) + "\n\n")


    if temp < 10:
        answer += ("Зараз дуже холодно, вдягайся як танк!")
    elif temp < 20:
        answer += ("Зараз холодно, вдягнись тепліше")
    else:
        answer += ("Зараз тепло, Вдягай що завгодно")

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)