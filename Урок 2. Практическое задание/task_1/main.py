"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений или другого инструмента извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import os
import re
import csv

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def data_collect():
    arr = []
    data_dir = os.path.join(CURRENT_DIR, '')
    file_source = [f for f in os.listdir(data_dir) if f.split('.')[1] == 'txt']

    for file_name in file_source:
        file_path = os.path.join(data_dir, file_name)

        with open(file_path, encoding='utf-8') as f:
            for i in f.readlines():
                arr += re.findall(r'^(\w[^:]+).*:\s+([^:\n]+)\s*$', i)

    return arr


def get_data():
    data = data_collect()
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for d in data:
        os_prod_list.append(d[1]) if d[0] == main_data[0][0] else None
        os_name_list.append(d[1]) if d[0] == main_data[0][1] else None
        os_code_list.append(d[1]) if d[0] == main_data[0][2] else None
        os_type_list.append(d[1]) if d[0] == main_data[0][3] else None

    for r in range(len(os_prod_list)):
        main_data.append([os_prod_list[r], os_name_list[r], os_code_list[r], os_type_list[r]])

    return main_data


def write_to_csv(file_path):
    data = get_data()

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

        for d in data:
            writer.writerow(d)


write_to_csv('data_report.csv')
