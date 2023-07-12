import datetime
import time
import random
import string
import os
import subprocess

if not os.path.exists("main"):
    if os.path.exists("tmain/tr.py"):
        subprocess.run(["python", "tmain/tr.py"])
    else:
        print("Не удалось найти файл tr.py")
else:
    os.remove("tmain/tr.py")
#COLOR2
class Back:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    RESET = '\033[49m'

class Style:
    BRIGHT = '\033[1m'
    DIM = '\033[2m'
    NORMAL = '\033[22m'
    RESET_ALL = '\033[0m'

class Fore:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m'
#Class.COLLOR
#Class= Back, Fore
#COLLOR= BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CUAN, WHITE, RESET
#Style.COLLOR2
#COLLOR2= BRIGHT, DIM, NORMAL, RESET_ALL
with open("Admin/setting.txt", "r") as f:
    for line in f:
        if "file_log" in line:
            file_log = line.strip().split("=")[1].strip()

def file():
    if not os.path.exists(file_log):
        open(file_log, "w").close()

logging_enabled=False #Рекомендуется False так как True нагружает память и процесор а если не нагружает то он может уничтожить память

class test1:
    class test1:
        def log_true(success, write_to_log=True):
            if write_to_log:
                with open(file_log, "a") as file:
                    file.write(f"TEMP LOG DATE={datetime.datetime.now()}: \n{'Успешно создан' if success else 'Ошибка создание'}\n")

        def generate_username():
            letters = string.ascii_letters + string.digits
            username = ''.join(random.choice(letters) for i in range(2))
            return username

        def generate_password():
            letters = string.ascii_letters + string.digits
            password = ''.join(random.choice(letters) for i in range(2))
            return password

        def generate_code():
            letters = string.ascii_letters + string.digits
            code = ''.join(random.choice(letters) for i in range(2))
            return code

    class test2:
        def test():
            count = 0
            while count < 25:
                username = test1.test1.generate_username()
                password = test1.test1.generate_password()
                code = test1.test1.generate_code()
                success = random.randint(0, 1)
                if success == 0:
                    print(Fore.RED + f"Ошибка создания: {username}; {password}; {code}!" + Back.RED + Style.RESET_ALL)
                    test1.test1.log_true(False, write_to_log=logging_enabled)
                if success == 1:
                    print(Fore.GREEN + f"Успешно создан: {username}; {password}; {code}!" + Back.GREEN + Style.RESET_ALL)
                    test1.test1.log_true(True, write_to_log=logging_enabled)
                    #time.sleep(0.05)
                    count += 1

class test2:
    file()
    def main():
        while True:
            mode = input("'' - Далее, (любая буква) - Стоп\n")
            if mode == "":
                test1.test2.test()
            else:
                break
