"""
Вам необходимо написать программу описания музеев. Для этого нужно объявить класс Museum, объекты которого формируются командой:
mus = Museum(название музея)
В объектах этого класса должны формироваться следующие локальные атрибуты:
name - название музея (строка);
exhibits - список экспонатов (изначально пустой список).
Сам класс Museum должен иметь методы:
add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка exhibits);
remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)
get_info_exhibit(self, indx) - получение информации об экспонате (строка) по индексу списка (нумерация с нуля).
Экспонаты представляются объектами своих классов. Для примера объявите в программе следующие классы экспонатов:
Picture - для картин;
Mummies - для мумий;
Papyri - для папирусов.
Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
p = Picture(название, художник, описание)            # локальные атрибуты: name - название; author - художник; descr - описание
m = Mummies(имя мумии, место находки, описание)      # локальные атрибуты: name - имя мумии; location - место находки; descr - описание
pr = Papyri(название папируса, датировка, описание)  # локальные атрибуты: name - название папируса; date - датировка (строка); descr - описание
Метод get_info_exhibit() класса Museum должен возвращать значение атрибута descr указанного экспоната в формате:
"Описание экспоната {name}: {descr}"
Например:
"Описание экспоната Девятый вал: Айвазовский написал супер картину."
Пример использования классов (в программе эти строчки писать не нужно - только для примера):
mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)
P.S. На экран ничего выводить не нужен
"""

from typing import List


class Exhibit:
    def __init__(self, name: str, descr: str):
        self.name = name
        self.descr = descr


class Picture(Exhibit):
    def __init__(self, name: str, author: str, descr: str):
        super().__init__(name, descr)
        self.author = author


class Mummies(Exhibit):
    def __init__(self, name: str, location: str, descr: str):
        super().__init__(name, descr)
        self.location = location


class Papyri(Exhibit):
    def __init__(self, name: str, date: str, descr: str):
        super().__init__(name, descr)
        self.date = date


class Museum:

    def __init__(self, name: str):
        self.name = name
        self.exhibits: List[Exhibit] = []

    def add_exhibit(self, obj: Exhibit):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj: Exhibit):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx: int):
        return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"

