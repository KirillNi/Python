"""Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое."""

import locale

words = ['сетевое программирование', 'сокет', 'декоратор']
file = 'test_file.txt'


def task_6(my_file, my_list):
    F_N = open(my_file, 'w')
    for word in my_list:
        F_N.write(f'{word}\n')
    F_N.close()

    with open('test_file.txt', encoding='utf-8') as f_n:
        default_encoding = locale.getpreferredencoding()
        print(default_encoding)
        with open('test_file.txt', 'r', encoding=default_encoding) as f_n_n:
            for line in f_n_n:
                print(line, end='')


task_6(file, words)
