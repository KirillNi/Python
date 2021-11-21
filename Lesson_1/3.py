"""Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""

words = ['attribute', 'класс', 'функция', 'type']


def task_3(my_list):
    for word in my_list:
        try:
            b_word = eval(f"b'{word}'")
            print(b_word, type(b_word))
        except SyntaxError:
            print(f'{word} - невозможно записать в байтовом типе.')


task_3(words)
