"""
 Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты этого класса создаются командой:

p = PhoneBook()
А сам класс должен иметь следующий набор методов:

add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:

note = PhoneNumber(number, fio)
где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра); fio - Ф.И.О. владельца номера (строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:

number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.

Пример использования классов (эти строчки в программе писать не нужно):

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""

class PhoneNumber:
    def __init__(self, number, fio: str):
        self._number = None
        self._fio = None
        self.number = number
        self.fio = fio

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, val):
        if 10000000000 <= val <= 99999999999:
            self._number = val

    @property
    def fio(self):
        return self._fio

    @fio.setter
    def fio(self, val):
        if isinstance(val, str):
            self._fio = val


class PhoneBook:

    def __init__(self):
        self.tel_books = []

    def add_phone(self, phone: PhoneNumber):
        self.tel_books.append(phone)

    def remove_phone(self, indx: int):
        self.tel_books.pop(indx)

    def get_phone_list(self):
        return self.tel_books

