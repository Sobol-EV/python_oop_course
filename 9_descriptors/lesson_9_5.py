"""
Необходимо написать программу для представления и управления расписанием телевизионного вещания. Для этого нужно объявить класс TVProgram, объекты которого создаются командой:

pr = TVProgram(название канала)
где название канала - это строка с названием телеканала.

В каждом объекте класса TVProgram должен формироваться локальный атрибут:

items - список из телепередач (изначально список пуст).

В самом классе TVProgram должны быть реализованы следующие методы:

add_telecast(self, tl) - добавление новой телепередачи в список items;
remove_telecast(self, indx) - удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее).

Каждая телепередача должна описываться классом Telecast, объекты которого создаются командой:

tl = Telecast(порядковый номер, название, длительность)
где порядковый номер - номер телепередачи в сетке вещания (от 1 и далее); название - наименование телепередачи; длительность - время телепередачи (в секундах - целое число).

Соответственно, в каждом объекте класса Telecast должны формироваться локальные приватные атрибуты:

__id - порядковый номер (целое число);
__name - наименование телепередачи (строка);
__duration - длительность телепередачи в секундах (целое число).

Для работы с этими приватными атрибутами в классе Telecast должны быть объявлены соответствующие объекты-свойства (property):

uid - для записи и считывания из локального атрибута __id;
name - для записи и считывания из локального атрибута __name;
duration - для записи и считывания из локального атрибута __duration.

Пример использования классов (эти строчки в программе писать не нужно):

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
"""


class Telecast:
    def __init__(self, uid: int, name: str, duration: int):
        self.__id = uid
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value: int):
        if isinstance(value, int) and value > 0:
            self.__id = value
        else:
            raise ValueError("UID must be a positive integer")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and value:
            self.__name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value: int):
        if isinstance(value, int) and value > 0:
            self.__duration = value
        else:
            raise ValueError("Duration must be a positive integer")


class TVProgram:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add_telecast(self, tl: Telecast):
        if not isinstance(tl, Telecast):
            raise TypeError("Expected a Telecast instance")
        self.items.append(tl)

    def remove_telecast(self, uid: int):
        self.items = [item for item in self.items if item.uid != uid]

