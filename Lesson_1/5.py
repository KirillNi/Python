"""Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице."""

import chardet
import subprocess

ARGS = [['ping', 'yandex.ru', '-n', '2'], ['ping', 'youtube.com', '-n', '2']]


def task_5(my_list):
    for arg in my_list:
        ping = subprocess.Popen(arg, stdout=subprocess.PIPE)
        for line in ping.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'))


task_5(ARGS)
