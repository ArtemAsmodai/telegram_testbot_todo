import telebot
import random
import settings

token = settings.token

bot = telebot.TeleBot(token)

RANDOM_TASKS = ["GO TO WORK", "GET FOOD", "SLEEP BEFORE 23:30"]

HELP = """
/help - справка.
/add - добавить задачу.
/show - все актуальные задачи.
/ToDO - задачи по дням.
/today - задачи на Сегодня.
/tomorrow - задачи на Завтра.
/other - Другие задачи"""

tasks = {}

#добавить задачу
def add_todo(date, task):
    if date in tasks:
        # date есть в словаре, доабвляем задачу
        tasks[date].append(task)
    else:
        # date none, create
        tasks[date] = []
        tasks[date].append(task)


#возьми след конструкцию и зарегистрируй как обработчик (с помощью этой функции я хочу обрабатывать команду хелп)
#команда хелп, бот отправляет в тот же чат откуда получил сообщение из переменной ХЕЛП
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message): # message.text = /print <date>
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        #для каждой задачи в списке который хранится в словаре
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)


#возврат эхо сообщений
# @bot.message_handler(content_types=["text"])
#def echo(message):
#    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)