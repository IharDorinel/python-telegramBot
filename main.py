import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('insert your token')


@bot.message_handler(commands=['start'])
def start_message(message):

    bot.reply_to(message, 'Привет! Я чат-бот, который будет напоминать тебе делать упражнения!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()


@bot.message_handler(commands=['fact'])
def fact_message(message):
    facts = ['Регулярные тренировки снижают калории',
             'Благодаря регулярным тренировкам улучшается самочувствие',
             'Регулярные тренировки способствуют улучшению когнитивных способностей']
    random_fact = random.choice(facts)
    bot.reply_to(message, random_fact)

@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = 'Ты можешь управлять мной, используя следующие команды: \n /start - начать \n /fact - любопытный факт \n /help - помощь'
    bot.reply_to(message, help_text)


def send_reminders(chat_id):
    first_rem = "13:55"
    second_rem = "15:30"
    last_rem = "17:30"

    while True:
        now = datetime.datetime.now().strftime('%H:%M')

        if now == first_rem or now == second_rem or now == last_rem:
            bot.send_message(chat_id, "Напоминание - сделай тренировку!")
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True)