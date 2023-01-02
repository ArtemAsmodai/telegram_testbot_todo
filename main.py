HELP = """
help - справка.
add - добавить задачу.
show - все актуальные задачи.
ToDO - задачи по дням.
today - задачи на Сегодня.
tomorrow - задачи на Завтра.
other - Другие задачи.
"""

tasks = []
today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "today":
        print(today)
    elif command == "tomorrow":
        print(tomorrow)
    elif command == "":
        print(other)
    elif command == "add":
        task = input("Введите задачу: ")
        tasks.append(task)
        time = input("На какой день задача: ")
        if time == "Сегодня":
          today.append(task)
        elif command == "Завтра":
          tomorrow.append(task)
        else:
          other.append(task)
        print("Задача добавлена.")
    elif command == "ToDO":
        print("Сегодня", today)
        print("Завтра", tomorrow)
        print("Остальное", other)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        break

print("Завершение работы")
