def register():
    print("Регистрация")
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    code = input("Введите код: ")
    with open(file_users, "r") as file:
        users = json.load(file)
    if username in users:
        print("Пользователь с таким именем уже зарегистрирован!")
        log_register(username, False)
    else:
        users[username] = {"password": password, "code": code, "attempts": 0, "blocked": False}
        with open(file_users, "w") as file:
            json.dump(users, file)
        print("Вы успешно зарегистрировались!")
        log_register(username, True)
        print("https://sites.google.com/view/modminecraft0/")

def login():
    print("Логин")
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    with open(file_users, "r") as file:
        users = json.load(file)
    if username not in users:
        print("Неверное имя пользователя!")
        log_login(username, False)
    elif users[username]["blocked"]:
        print("Ваша учетная запись заблокирована!")
    elif users[username]["password"] != password:
        if "attempts" not in users[username]:
            users[username]["attempts"] = 1
        else:
            users[username]["attempts"] += 1
        if users[username]["attempts"] >= 3:
            users[username]["blocked"] = True
            print("Ваша учетная запись заблокирована!")
        else:
            print("Неверный пароль!")
            log_login(username, False)
        with open(file_users, "w") as file:
            json.dump(users, file)
    else:
        print("Вы успешно вошли в систему!")
        log_login(username, True)
        print("https://sites.google.com/view/modminecraft0/")

def change():
    print("Смена пароля")
    username = input("Введите имя пользователя: ")
    code = input("Введите код для восстановления пароля: ")
    new_password = input("Введите новый пароль: ")
    with open(file_users, "r") as file:
        users = json.load(file)
    if username not in users:
        print("Неверное имя пользователя!")
        log_change(username, new_password, False)
    elif users[username]["code"] != code:
        print("Неверный код для восстановления пароля!")
        log_change(username, new_password, False)
    else:
        users[username]["password"] = new_password
        with open(file_users, "w") as file:
            json.dump(users, file)
        print("Пароль успешно изменен!")
        log_change(username, new_password, True)
