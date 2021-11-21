"""Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и
длину соответствующих переменных."""

words = [b'class', b'function', b'method']


def task_2(my_list):
    for word in my_list:
        print(f'Слово: {word}, Тип: {type(word)}, Длина: {len(word)}')


task_2(words)
