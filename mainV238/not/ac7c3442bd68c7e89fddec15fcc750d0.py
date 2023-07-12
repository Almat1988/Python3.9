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
            return view_admin()

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
            return view_admin()

def view_admin():
    while True:
        txt = input("TXT файлы:\n1 - Обзор log\n2 - Очистка log\n3 - Выход\n---> ")
        if txt == "1":
            txt_log_view()
        elif txt == "2":
            txt_log_clear()
        elif txt == "3":
            return main()

def txt_log_login():
        admin_username = input("Имя админа: ")
        admin_password = input("Пароль админа: ")
        admin_username_hash = hashlib.sha3_256(admin_username.encode()).hexdigest()
        admin_password_hash = hashlib.sha3_256(admin_password.encode()).hexdigest()
        if admin_username_hash == adm_user_hash:
            if admin_password_hash == adm_pass_hash:
                return view_admin()
