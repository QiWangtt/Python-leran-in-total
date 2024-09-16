# _*_ coding: utf-8 _*_
# @Time: 02.09.2024 15:50
# @Author: Qi Wang
# @File: 137_Bsp_LoginPage
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

class LoginPage:
    def __init__(self, username, password, code):
        self.username = username
        self.password = password
        self.code = code
        self.button = 'login'

    def login(self):
        print(f'1. input username: {self.username}')
        print(f'2. input password: {self.username}')
        print(f'3. input code: {self.code}')
        print(f'4. press button: {self.button}')


login = LoginPage('admin', '1568413', '6666')
login.login()
