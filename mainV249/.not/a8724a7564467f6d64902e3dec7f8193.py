def unlock_account():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    code = input("Введите код: ")
    with open(file_users, "r") as file:
        users = json.load(file)
    if username not in users:
        print("Неверное имя пользователя!")
    elif "code" not in users[username] or users[username]["code"] != code:
        print("Неверный код разблокировки!")
    elif "password" not in users[username] or users[username]["password"] != password:
        print("Неверный пароль!")
    elif "blocked" not in users[username] or not users[username]["blocked"]:
        print("Аккаунт не заблокирован!")
    else:
        users[username]["blocked"] = False
        users[username]["attempts"] = 0
        with open(file_users, "w") as file:
            json.dump(users, file)
        print("Аккаунт успешно разблокирован!")

def code_pass():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    with open(file_users, "r") as file:
        users = json.load(file)
    if username in users:
        if users[username]["password"] == password:
            code = users[username]["code"]
            print(f"Ваш код: {code}")
            log_pass(username, None, code, True)
        else:
            print("Неверный пароль")
            log_pass(username, None, code, False)
    else:
        print("Неверное имя пользователя")
        log_pass(username, None, code, False)

def password_pass():
    username = input("Введите имя пользователя: ")
    code = input("Введите код: ")
    with open(file_users, "r") as file:
        users = json.load(file)
    if username in users:
        password = users[username]["password"]
        if users[username]["code"] == code:
            print(f"Ваш пароль: {password}")
            log_pass(username, password, None, True)
        else:
            print("Неверный код!")
            log_pass(username, password, None, False)
    else:
        print("Неверное имя пользователя!")
        log_pass(username, password, None, False)

def users():
    username = input("Имя: ")
    with open(file_users, "r") as file:
        users = json.load(file)
    if username in users:
        password = users[username]["password"]
        code = users[username]["code"]
        print(f"Пароль: {password}")
        print(f"Код: {code}")
        log_pass(username, None, None, True)

def admin():
    while True:
        adm = input("Админ панель:\n1 - Показ кода\n2 - Показ пароля\n3 - Разблокировать акаунт\n4 - Выход\n---> ")
        if adm == "1":
            code_pass()
        elif adm == "2":
            password_pass()
        elif adm == "3":
            unlock_account()
        elif adm == "4":
            return
        elif adm == "none":
            users()

def admin_login():
    admin_login = input("Админ логин: ")
    username_hash = hashlib.sha512(admin_login.encode()).hexdigest()
    if username_hash == adm_hash:
        admin()
    else:
        print("Неверный логин!")
