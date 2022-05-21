"""Для Windows"""
import subprocess
import time

PROCESSES = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, '
                   'x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        PROCESSES.append(subprocess.Popen('cmd  python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))

        time.sleep(1)
        for i in range(2):
            PROCESSES.append(subprocess.Popen(f'cmd  python client.py ', creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif ACTION == 'x':
        while PROCESSES:
            VICTIM = PROCESSES.pop()
            VICTIM.terminate()
