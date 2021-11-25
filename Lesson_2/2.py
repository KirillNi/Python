"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = {'Товар': item,
             'Количество': quantity,
             'Цена': price,
             'Покупатель': buyer,
             'Дата': date}

    with open('orders.json', encoding='utf-8') as f_n:
        orders_dict = json.load(f_n)
        orders_dict['orders'].append(order)

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(orders_dict, f_n, indent=4)


write_order_to_json('Товар_1', 5, 2900, 'user_1', '10-10-2010')
write_order_to_json('Товар_2', 90, 21, 'user_2', '28-08-2015')
write_order_to_json('Товар_3', 19, 999, 'user_3', '17-01-2019')
