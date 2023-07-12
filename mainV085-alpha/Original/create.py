#CREATE
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
