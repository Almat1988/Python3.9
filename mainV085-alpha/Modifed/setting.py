#Пожалуиста не редактируй любой фаил
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
            #os.remove(f"Admin/setting{i}.txt")
        #os.remove(f"Admin/setting{counter}.txt")
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
