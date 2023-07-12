import os
import shutil

# Создание папки "main", если ее не существует
if not os.path.exists("tmain/main"):
    os.makedirs("tmain/main")

# Создание папки "not" внутри "main", если ее не существует
if not os.path.exists("tmain/main/not"):
    os.makedirs("tmain/main/not")

# Поиск и перемещение файлов в папку "not"
for filename in ["view_log.py", "telegram.py", "setting.py", "modules.py", "log.py", "create.py", "all.py", "admin.py"]:
    if os.path.exists(f"tmain/{filename}"):
        shutil.move(f"tmain/{filename}", "tmain/main/not")
    else:
        print(f"Нету фаилов для перемещений: {filename}")

# Поиск и перемещение файлов в папку "main"
for filename in ["main.py", "test.py", "default.py", "text.txt"]:
    if os.path.exists(f"tmain/{filename}"):
        shutil.move(f"tmain/{filename}", "tmain/main")
    else:
        print(f"Нету фаилов для перемещений: {filename}")
