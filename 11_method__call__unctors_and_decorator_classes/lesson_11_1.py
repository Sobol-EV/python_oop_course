"""Объявите класс RandomPassword для генерации случайных паролей. Объекты этого класса должны создаваться командой:
rnd = RandomPassword(psw_chars, min_length, max_length)
где psw_chars - строка из разрешенных в пароле символов; min_length, max_length - минимальная и максимальная длина генерируемых паролей.
Непосредственная генерация одного пароля должна выполняться командой:
psw = rnd()
где psw - ссылка на строку длиной в диапазоне [min_length; max_length] из случайно выбранных символов строки psw_chars.
С помощью генератора списка (list comprehension) создайте список lst_pass из трех сгенерированных паролей объектом rnd класса RandomPassword, созданного с параметрами:
min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
P.S. Выводить на экран ничего не нужно, только создать список из паролей.
P.P.S. Дополнительное домашнее задание: попробуйте реализовать этот же функционал с использованием замыканий функций.
"""

from random import randint
from typing import List


class RandomPassword:
    def __init__(self, psw_chars: str, min_length: int, max_length: int):
        self.__psw_chars = psw_chars
        self.__min_length = min_length
        self.__max_length = max_length

    def __gen_random_symbol(self) -> str:
        return self.__psw_chars[randint(0, len(self.__psw_chars) - 1)]

    def __gen_random_password(self) -> str:
        length = randint(self.__min_length, self.__max_length)
        return "".join(self.__gen_random_symbol() for _ in range(length))

    def __call__(self, *args, **kwargs) -> str:
        return self.__gen_random_password()


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)

lst_pass: List[str] = [rnd() for _ in range(3)]
