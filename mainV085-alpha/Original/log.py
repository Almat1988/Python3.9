#LOG
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
