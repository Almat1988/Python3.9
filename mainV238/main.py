print("Запуск")
exec(open("main/not/2f9851c5ff8524a99c0b3f855f8693f5.py").read())

def main():
    while True:
        mode = input("Выберите режим:\n1 - Регистрация\n2 - Вход\n3 - Восстановление пароля\n4 - Admin\n5 - Log\n6 - Информация\n7 - Выход\n--> ")
        if mode == "1":
            register()
        elif mode == "2":
            login()
        elif mode == "3":
            change()
        elif mode == "4":
            admin_login()
        elif mode == "5":
            txt_log_login()
        elif mode == "6":
            info()
        elif mode == "7":
            check_internet()
            break
        else:
            print("Неверный режим, попробуйте еще раз!")

main()
