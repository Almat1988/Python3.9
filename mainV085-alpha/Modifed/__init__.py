import os
import shutil

if not os.path.exists("main/not"):
    os.makedirs("main/not")

for filename in ["view_log.py", "telegram.py", "setting.py", "modules.py", "log.py", "create.py", "all.py", "admin.py"]:
    if os.path.exists(f"tmain/{filename}"):
        shutil.move(f"tmain/{filename}", "main/not")
    else:
        print(f"Нету фаилов для перемещений: {filename}")

# Поиск и перемещение файлов в папку "main"
for filename in ["main.py", "test.py", "default.py", "text.txt"]:
    if os.path.exists(f"tmain/{filename}"):
        shutil.move(f"tmain/{filename}", "main")
    else:
        print(f"Нету фаилов для перемещений: {filename}")
