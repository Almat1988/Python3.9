import os
import json
import datetime
import hashlib
import string
import random
import telegram
import asyncio

import urllib.request
import time

if not os.path.exists("Admin"):
    os.mkdir("Admin")

if not os.path.exists("Admin/log"):
    os.mkdir("Admin/log")

def file_all():
    if not os.path.exists(file_log_register):
        open(file_log_register, "w").close()
    if not os.path.exists(file_log_login):
        open(file_log_login, "w").close()
    if not os.path.exists(file_log_change):
        open(file_log_change, "w").close()
    if not os.path.exists(file_log_pass):
        open(file_log_pass, "w").close()
    if not os.path.exists(file_users):
        with open(file_users, "w") as f:
            json.dump({}, f)

count = 0
while count < 2:
    if not os.path.exists('Admin/setting.txt'):
        with open('Admin/setting.txt', 'w') as f:
            f.write('log_register=Admin/log/register.log\n')
            f.write('log_login=Admin/log/login.log\n')
            f.write('log_change=Admin/log/change.log\n')
            f.write('log_pass=Admin/log/pass.log\n')
            f.write('file_log=Admin/log/log.log\n')
            f.write('file_users=Admin/users.json\n')
            f.write('adm_hash=a74fff5a40cb0865f0ed2be4d5fc63565e347c6260093f87c94d0c3855dbe2f8\n')
            f.write('adm_user_hash=b6e3d128948810ff69860a55f442fb12291fd24a01c0f4ae97a075d9465391ba\n')
            f.write('adm_pass_hash=954525cbd77132f2d5c7271b3219c6615503089518081dbe82b728a03f9b61b9\n')
    with open('Admin/setting.txt', 'r') as file:
        settings = file.read()
    if settings != "log_register=Admin/log/register.log\nlog_login=Admin/log/login.log\nlog_change=Admin/log/change.log\nlog_pass=Admin/log/pass.log\nfile_log=Admin/log/log.log\nfile_users=Admin/users.json\nadm_hash=a74fff5a40cb0865f0ed2be4d5fc63565e347c6260093f87c94d0c3855dbe2f8\nadm_user_hash=b6e3d128948810ff69860a55f442fb12291fd24a01c0f4ae97a075d9465391ba\nadm_pass_hash=954525cbd77132f2d5c7271b3219c6615503089518081dbe82b728a03f9b61b9\n":
        counter = 1
        while os.path.exists(f"Admin/setting{counter}.txt"):
            counter += 1
        os.rename("Admin/setting.txt", f"Admin/setting{counter}.txt")
        for i in range(1, counter):
            os.remove(f"Admin/setting{i}.txt")
        os.remove(f"Admin/setting{counter}.txt")
    count += 1

with open("Admin/setting.txt", "r") as f:
    for line in f:
        if "log_register" in line:
            file_log_register = line.strip().split("=")[1].strip()
        if "log_login" in line:
            file_log_login = line.strip().split("=")[1].strip()
        if "log_change" in line:
            file_log_change = line.strip().split("=")[1].strip()
        if "log_pass" in line:
            file_log_pass = line.strip().split("=")[1].strip()
        if "adm_hash" in line:
            adm_hash = line.strip().split("=")[1].strip()
        if "adm_user_hash" in line:
            adm_user_hash = line.strip().split("=")[1].strip()
        if "adm_pass_hash" in line:
            adm_pass_hash = line.strip().split("=")[1].strip()
        if "file_users" in line:
            file_users = line.strip().split("=")[1].strip()
        if "file_log" in line:
            file_log = line.strip().split("=")[1].strip()

class log:
    def log_register(username, success):
        with open(file_log_register, "a") as file:
            file.write(f"REGISTER DATE={datetime.datetime.now()}; \nuser= {username}: {'УСПЕХ' if success else 'ОШИБКА'}\n\n")

    def log_login(username, success):
        with open(file_log_login, "a") as file:
            file.write(f"LOGIN DATE={datetime.datetime.now()}; \nuser= {username}: {'УСПЕХ' if success else 'ОШИБКА'}\n\n")

    def log_change(username, new_password, success):
        with open(file_log_change, "a") as file:
            file.write(f"CHANGE DATE={datetime.datetime.now()}; \nuser= {username};  new_pass= {new_password}: {'УСПЕХ' if success else 'ОШИБКА'}\n\n")

    def log_pass(username, password, code, success):
        with open(file_log_pass, "a") as file:
            file.write(f"PASS DATE={datetime.datetime.now()}; \nuser= {username}; pass= {password}; code= {code}: {'УСПЕХ' if success else 'ОШИБКА'}\n\n")

class default:
    def register():
        print("Регистрация")
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        code = input("Введите код: ")
        with open(file_users, "r") as file:
            users = json.load(file)
        if username in users:
            print("Пользователь с таким именем уже зарегистрирован!")
            log.log_register(username, False)
        else:
            users[username] = {"password": password, "code": code, "attempts": 2, "blocked": False}
            with open(file_users, "w") as file:
                json.dump(users, file)
            print("Вы успешно зарегистрировались!")
            log.log_register(username, True)
            print("https://sites.google.com/view/modminecraft0/")

    def login():
        print("Логин")
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        with open(file_users, "r") as file:
            users = json.load(file)
        if username not in users:
            print("Неверное имя пользователя!")
            log.log_login(username, False)
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
                log.log_login(username, False)
            with open(file_users, "w") as file:
                json.dump(users, file)
        else:
            print("Вы успешно вошли в систему!")
            log.log_login(username, True)
            print("https://sites.google.com/view/modminecraft0/")

    def change_password():
        print("Смена пароля")
        username = input("Введите имя пользователя: ")
        code = input("Введите код для восстановления пароля: ")
        new_password = input("Введите новый пароль: ")
        with open(file_users, "r") as file:
            users = json.load(file)
        if username not in users:
            print("Неверное имя пользователя!")
            log.log_change(username, new_password, False)
        elif users[username]["code"] != code:
            print("Неверный код для восстановления пароля!")
            log.log_change(username, new_password, False)
        else:
            users[username]["password"] = new_password
            with open(file_users, "w") as file:
                json.dump(users, file)
            print("Пароль успешно изменен!")
            log.log_change(username, new_password, True)

class view_log:
    def txt_log_clear():
        while True:
            txt = input("TXT файлы очистка:\n1 - Очистить register.log\n2 - Очистить login.log\n3 - Очистить change.log\n4 - Очистить pass.log\n5 - Назад\n---> ")
            if txt == "1":
                with open(file_log_register, "w") as f:
                    f.write("")
            elif txt == "2":
                with open(file_log_login, "w") as f:
                    f.write("")
            elif txt == "3":
                with open(file_log_change, "w") as f:
                    f.write("")
            elif txt == "4":
                with open(file_log_pass, "w") as f:
                    f.write("")
            elif txt == "5":
                return view_log.view_main()

    def txt_log_view():
        while True:
            txt = input("TXT файлы обзор:\n1 - register.log\n2 - login.log\n3 - change.log\n4 - pass.log\n5 - Назад\n---> ")
            if txt == "1":
                with open(file_log_register, "r") as f:
                     contents = f.read()
                print(contents)
            elif txt == "2":
                with open(file_log_login, "r") as f:
                    contents = f.read()
                print(contents)
            elif txt == "3":
                with open(file_log_change, "r") as f:
                    contents = f.read()
                print(contents)
            elif txt == "4":
                with open(file_log_pass, "r") as f:
                    contents = f.read()
                print(contents)
            elif txt == "5":
                return view_log.view_main()

    def view_main():
        while True:
            txt = input("TXT файлы:\n1 - Обзор log\n2 - Очистка log\n3 - Выход\n---> ")
            if txt == "1":
                view_log.txt_log_view()
            elif txt == "2":
                view_log.txt_log_clear()
            elif txt == "3":
                return main()

    def txt_log_login():
        admin_username = input("Имя админа: ")
        admin_password = input("Пароль админа: ")
        admin_username_hash = hashlib.sha3_256(admin_username.encode()).hexdigest()
        admin_password_hash = hashlib.sha3_256(admin_password.encode()).hexdigest()
        if admin_username_hash == adm_user_hash:
            if admin_password_hash == adm_pass_hash:
                return view_log.view_main()

class admin:
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
                log.log_pass(username, None, code, True)
            else:
                print("Неверный пароль")
                log.log_pass(username, None, code, False)
        else:
            print("Неверное имя пользователя")
            log.log_pass(username, None, code, False)

    def password_pass():
        username = input("Введите имя пользователя: ")
        code = input("Введите код: ")
        with open(file_users, "r") as file:
            users = json.load(file)
        if username in users:
            password = users[username]["password"]
            if users[username]["code"] == code:
                print(f"Ваш пароль: {password}")
                log.log_pass(username, password, None, True)
            else:
                print("Неверный код!")
                log.log_pass(username, password, None, False)
        else:
            print("Неверное имя пользователя!")
            log.log_pass(username, password, None, False)

    def users():
        username = input("Имя: ")
        with open(file_users, "r") as file:
            users = json.load(file)
        if username in users:
            password = users[username]["password"]
            code = users[username]["code"]
            print(f"Пароль: {password}")
            print(f"Код: {code}")
            log.log_pass(username, None, None, True)

    def admin():
        while True:
            adm = input("Админ панель:\n1 - Показ кода\n2 - Показ пароля\n3 - Разблокировать акаунт\n4 - Выход\n---> ")
            if adm == "1":
                admin.code_pass()
            elif adm == "2":
                admin.password_pass()
            elif adm == "3":
                admin.unlock_account()
            elif adm == "4":
                return
            elif adm == "none":
                admin.users()

    def admin_login():
        admin_login = input("Админ логин: ")
        username_hash = hashlib.sha3_256(admin_login.encode()).hexdigest()
        if username_hash == adm_hash:
            admin.admin()
        else:
            print("Неверный логин!")

class telegram1:
    def telegram_message():
        print('То что здесь напечатали не сохраняются! Чтобы не печатать каждый раз бот токен и чат id, можно изменить: input("Изменить это на ваш бот токен!") и input("Изменить это на ваш чат id!: ")')
        bot_token = input("Изменить это на ваш бот токен!")
        chat_id = input("Изменить это на ваш чат id!: ")
        bot = telegram.Bot(token=bot_token)
        async def send_message():
            await bot.send_message(chat_id=chat_id, text=f"Log time: {datetime.datetime.now()}")
            with open(file_log_register, 'r') as f:
                register_log = f.read()
                if len(register_log) > 4000:
                    for i in range(0, len(register_log), 4000):
                        await bot.send_message(chat_id=chat_id, text=f'Register log:\n{register_log[i:i+4000]}')
                else:
                    await bot.send_message(chat_id=chat_id, text=f'Register log:\n{register_log}')
            with open(file_log_login, 'r') as f:
                login_log = f.read()
                if len(login_log) > 4000:
                    for i in range(0, len(login_log), 4000):
                        await bot.send_message(chat_id=chat_id, text=f'Login log:\n{login_log[i:i+4000]}')
                else:
                    await bot.send_message(chat_id=chat_id, text=f'Login log:\n{login_log}')
            with open(file_log_change, 'r') as f:
                change_log = f.read()
                if len(change_log) > 4000:
                    for i in range(0, len(change_log), 4000):
                        await bot.send_message(chat_id=chat_id, text=f'Change log:\n{change_log[i:i+4000]}')
                else:
                    await bot.send_message(chat_id=chat_id, text=f'Change log:\n{change_log}')
            with open(file_log_pass, 'r') as f:
                pass_log = f.read()
                if len(pass_log) > 4000:
                    for i in range(0, len(pass_log), 4000):
                        await bot.send_message(chat_id=chat_id, text=f'Pass log:\n{pass_log[i:i+4000]}')
                else:
                    await bot.send_message(chat_id=chat_id, text=f'Pass log:\n{pass_log}')
            with open(file_log, 'r') as f:
                log_log = f.read()
                if len(log_log) > 4000:
                    for i in range(0, len(log_log), 4000):
                        await bot.send_message(chat_id=chat_id, text=f'Log log:\n{log_log[i:i+4000]}')
                else:
                    await bot.send_message(chat_id=chat_id, text=f'Log log:\n{log_log}')
        asyncio.run(send_message())

    def check_internet_connection():
        try:
            urllib.request.urlopen('http://google.com')
            return True
        except:
            return False

    def check_internet():
        if telegram1.check_internet_connection():
            telegram1.telegram_message()
        else:
            print("Нету подключение к интернету!")

print("Запуск")
def main():
    file_all()
    while True:
        mode = input("Выберите режим:\n1 - Регистрация\n2 - Вход\n3 - Восстановление пароля\n4 - Admin\n5 - Log\n6 - Выход\n--> ")
        if mode == "1":
            default.register()
        elif mode == "2":
            default.login()
        elif mode == "3":
            default.change_password()
        elif mode == "4":
            admin.admin_login()
        elif mode == "5":
            view_log.txt_log_login()
        elif mode == "6":
            telegram1.check_internet()
            break
        else:
            print("Неверный режим, попробуйте еще раз!")

main()
