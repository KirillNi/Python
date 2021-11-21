"""Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
представления в байтовое и выполнить обратное преобразование (используя методы encode и decode)"""

words = ['разработка', 'администрирование', 'protocol', 'standard']


def task_4(my_list):
    for word in my_list:
        enc_word = word.encode('utf-8')
        dec_word = enc_word.decode('utf-8')
        print(f'Слово: {word}, В байты: {enc_word}, В строку: {dec_word}')


task_4(words)
