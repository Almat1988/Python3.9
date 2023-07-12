print("Запуск")
import os
import subprocess

if not os.path.exists("main/main.py"):
    if os.path.exists("tmain/tr.py"):
        subprocess.run(["python", "tmain/tr.py"])
    else:
        print("Не удалось найти файл tr.py")
else:
    os.remove("tmain/tr.py")
exec(open("main/not/all.py").read())
#MAIN FUNCTION
def main():
    file_all()
    while True:
        mode = input("Выберите режим:\n1 - Регистрация\n2 - Вход\n3 - Восстановление пароля\n4 - Admin\n5 - Log\n6 - Выход\n--> ")
        if mode == "1":
            register()
        elif mode == "2":
            login()
        elif mode == "3":
            change_password()
        elif mode == "4":
            admin_login()
        elif mode == "5":
            txt_log_login()
        elif mode == "6":
            break
        elif mode == "7":
            check_internet()
        else:
            print("Неверный режим, попробуйте еще раз!")
        
main()
