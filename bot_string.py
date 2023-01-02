command = "/add 12.12.2020 Add asdsad"

splitted_command = command.split(maxsplit=2)
print(splitted_command)

date = splitted_command[1]
task = splitted_command[2]

print (date, task)