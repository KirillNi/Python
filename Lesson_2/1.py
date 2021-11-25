"""
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
"""

import re
import csv
from chardet import detect

FILES_LST = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def get_data(files):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    list_without_headers = [os_prod_list, os_name_list, os_code_list, os_type_list]
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for file in files:
        with open(file, 'rb') as f_n:
            CONTENT = f_n.read()
        ENCODING = detect(CONTENT)['encoding']

        with open(file, 'r', encoding=ENCODING) as f_n:
            CONTENT = f_n.read()
            os_prod = re.findall(r'Изготовитель системы:(.+)', CONTENT)
            os_name = re.findall(r'Название ОС:(.+)', CONTENT)
            os_code = re.findall(r'Код продукта:(.+)', CONTENT)
            os_type = re.findall(r'Тип системы:(.+)', CONTENT)
            os_prod_list.append(os_prod[0].lstrip())
            os_name_list.append(os_name[0].lstrip())
            os_code_list.append(os_code[0].lstrip())
            os_type_list.append(os_type[0].lstrip())

    for i in range(len(list_without_headers[0])):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

    return main_data


def write_to_csv(csv_file):
    DATA = get_data(FILES_LST)
    with open(csv_file, 'w', encoding='utf-8') as f_n:
        F_N_WRITER = csv.writer(f_n)
        F_N_WRITER.writerows(DATA)


write_to_csv('task_1.csv')
