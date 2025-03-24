import unittest
from unittest.mock import patch
import tkinter as tk
from views import LoginView


class TestLoginView(unittest.TestCase):
    @patch('controllers.SecretaryController.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True  # Мокаем успешный логин

        root = tk.Tk()
        login_view = LoginView(root)

        login_view.username_entry.insert(0, "abc")
        login_view.password_entry.insert(0, "cba")
        login_view.login()  # вызываем метод входа

        # Проверяем, что окно закрывается после успешного входа
        self.assertFalse(root.winfo_exists())  # Окно должно быть закрыто

    @patch('controllers.SecretaryController.authenticate')
    def test_login_failure(self, mock_authenticate):
        mock_authenticate.return_value = False  # Мокаем неуспешный логин

        root = tk.Tk()
        login_view = LoginView(root)

        login_view.username_entry.insert(0, "wrong")
        login_view.password_entry.insert(0, "wrong")
        login_view.login()  # вызываем метод входа

        # Проверяем, что появляется сообщение об ошибке
        # Здесь можно проверить, что messagebox.showerror был вызван
        with self.assertRaises(Exception):
            login_view.login()


if __name__ == '__main__':
    unittest.main()