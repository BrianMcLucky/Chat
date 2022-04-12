# Задание 5.
#
# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
# преобразовать результаты из байтовового в строковый тип на кириллице.
#
# Подсказки:
# --- используйте модуль chardet, иначе задание не засчитается!!!
import subprocess
import chardet

ping_list = ['ping', 'yandex.ru']

ping_proc = subprocess.Popen(ping_list, stdout=subprocess.PIPE)
for i in ping_proc.stdout:
    res = chardet.detect(i)
    i = i.decode(res['encoding']).encode('utf-8')
    print(i.decode('utf-8'))

ping_list2 = ['ping', 'youtube.com']

ping_proc2 = subprocess.Popen(ping_list2, stdout=subprocess.PIPE)
for i in ping_proc2.stdout:
    res = chardet.detect(i)
    i = i.decode(res['encoding']).encode('utf-8')
    print(i.decode('utf-8'))

