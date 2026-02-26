# Модуль авторизации
def login(username, password):
    if username == "admin" and password == "123":
        return "Вход выполнен"
    else:
        return "Ошибка входа"
