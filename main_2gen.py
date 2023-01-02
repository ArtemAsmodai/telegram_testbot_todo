import random

HELP = """
help - справка.
add - добавить задачу.
show - все актуальные задачи.
ToDO - задачи по дням.
today - задачи на Сегодня.
tomorrow - задачи на Завтра.
other - Другие задачи.
"""

RANDOM_TASKS = ["GO TO WORK", "GET FOOD", "SLEEP BEFORE 23:30"]

tasks = {

}

run = True

def add_todo(date, task):
    if date in tasks:
        # date есть в словаре, доабвляем задачу
        tasks[date].append(task)
    else:
        # date none, create
        tasks[date] = []
        tasks[date].append(task)
    print("Задача ", task, " добавлена на ", date)

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Напишите день для отображения задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("No date!")
    elif command == "add":
        task = input("Введите задачу: ")
        date = input("На какой день задача: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    #elif command = "random_date":
        #add_todo(RANDOM_DATE, RANDOM_TASK)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        break

print("Завершение работы")
