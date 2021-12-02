"""Тесты сервера"""

import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '...'))

from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, RESPONDEFAULT_IP_ADDRESSSE
from server import process_client_message


class TestServer(unittest.TestCase):
    err_dict = {
        RESPONDEFAULT_IP_ADDRESSSE: 400,
        ERROR: "Bad Request"
    }
    ok_dict = {RESPONSE: 200}

    def test_ok_check(self):
        """Корректный запрос"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: "Guest"}}), self.ok_dict)

    def test_no_action(self):
        """Ошибка если нет действия"""
        self.assertEqual(process_client_message(
            {TIME: '1.1', USER: {ACCOUNT_NAME: "Guest"}}), self.err_dict)

    def test_wrong_action(self):
        """Ошибка при неизвестном действии"""
        self.assertEqual(process_client_message(
            {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: "Guest"}}), self.err_dict)

    def test_no_time(self):
        """Ошибка если нет времени"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: "Guest"}}), self.err_dict)

    def test_no_user(self):
        """Ошибка если не пользователя"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}), self.err_dict)

    def test_unknown_user(self):
        """Ошибка при неизвестном пользователе"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1', USER: {ACCOUNT_NAME: "Unknown"}}), self.err_dict)


if __name__ == '__main__':
    unittest.main()







