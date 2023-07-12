codes="log_register=Admin/log/register.log\nlog_login=Admin/log/login.log\nlog_change=Admin/log/change.log\nlog_pass=Admin/log/pass.log\nfile_log=Admin/log/log.log\nfile_users=Admin/users.json\nadm_hash=2a58ad94cf5bb0c3a9469767af0d96cd14e0e64896b007ae9f1f38cafe3a910978aefc907e0c7fbe5a06741bc1bf74528ee11eaa228acd792a823c7507ad02e5\nadm_user_hash=1bd36a45bd095e6167893be8b7d6acfb159e23759dbe060eff3a09401c958f87dc634d0497f6bbc8c39a7b36ef52cf293aa9cdeed90afc1157cfe015afee74a5\nadm_pass_hash=b8a59dc0ccab9e8c864a220ddccb579e9cb74bfa51851766b67206c85d3e37be048a483eb8c25dc702047a2edd02926f7f2a6c065b1f817df934c2a1f0284059\n"

for i in range(1):
    if not os.path.exists('Admin/setting.txt'):
        with open('Admin/setting.txt', 'w') as f:
            f.write(codes)
    with open('Admin/setting.txt', 'r') as file:
        settings = file.read()
    if settings != codes:
        counter = 1
        while os.path.exists(f"Admin/setting{counter}.txt"):
            counter += 1
        os.rename("Admin/setting.txt", f"Admin/setting{counter}.txt")
        for i in range(1, counter):
            os.remove(f"Admin/setting{i}.txt")
        os.remove(f"Admin/setting{counter}.txt")

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
