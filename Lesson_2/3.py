"""
3. Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
"""

import yaml

DATA_DICT = {'Список': ['первый', 'второй', 'третий'],
             'Целое число': 1500,
             'Словарь': {'Ключ_1': 'λ',
                         'Ключ_2': 'π',
                         'Ключ_3': 'β'}
             }


def task_3(data):
    with open('file.yaml', 'w', encoding='utf-8') as f_n:
        yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)


task_3(DATA_DICT)
