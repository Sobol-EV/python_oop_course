"""
Необходимо объявить класс Bag (рюкзак), объекты которого будут создаваться командой:

bag = Bag(max_weight)
где max_weight - максимальный суммарный вес вещей, который выдерживает рюкзак (целое число).

В каждом объекте этого класса должен создаваться локальный приватный атрибут:

__things - список вещей в рюкзаке (изначально список пуст).

Сам же класс Bag должен иметь объект-свойство:

things - для доступа к локальному приватному атрибуту __things (только для считывания, не записи).

Также в классе Bag должны быть реализованы следующие методы:

add_thing(self, thing) - добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление не происходит);
remove_thing(self, indx) - удаление предмета по индексу списка __things;
get_total_weight(self) - возвращает суммарный вес предметов в рюкзаке.

Каждая вещь описывается как объект класса Thing и создается командой:

t = Thing(название, вес)
где название - наименование предмета (строка); вес - вес предмета (целое или вещественное число).

В каждом объекте класса Thing должны формироваться локальные атрибуты:

name - наименование предмета;
weight - вес предмета.

Пример использования классов (эти строчки в программе писать не нужно):

bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
"""

from typing import Union


class ValidateBase:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate:
            setattr(instance, self.name, value)

    def validate(self, value):
        raise NotImplemented


class ValidateString(ValidateBase):

    def validate(self, value):
        return isinstance(value, str)


class ValidateIntFloat(ValidateBase):

    def validate(self, value):
        return isinstance(value, int) or isinstance(value, float)


class ValidateInt(ValidateBase):

    def validate(self, value):
        return isinstance(value, int)


class Thing:
    name = ValidateString()
    weight = ValidateIntFloat()

    def __init__(self, name: str, weight: Union[float, int]):
        self.name = name
        self.weight = weight


class Bag:
    max_weight = ValidateInt()

    def __init__(self, max_weight: int):

        self.max_weight = max_weight

        self.__things = []
        self.__current_weight = 0

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing: Thing):
        if (isinstance(thing, Thing) and
                (thing.weight <= self.max_weight) and
                ((self.max_weight - self.get_total_weight()) >= thing.weight)):
            self.__current_weight += thing.weight
            self.__things.append(thing)

    def remove_thing(self, indx: int):
        if isinstance(indx, int) and (0 <= indx <= len(self.__things)):
            self.__current_weight -= self.__things[indx].weight
            self.__things.pop(indx)

    def get_total_weight(self) -> int:
        return self.__current_weight

