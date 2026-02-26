# Пользовательский интерфейс
from auth import login
from db import get_tasks

print("=== Добро пожаловать ===")
user = input("Логин: ")
pwd = input("Пароль: ")

result = login(user, pwd)
print(result)

if "Вход выполнен" in result:
    print("Ваши задачи:", get_tasks())
