"""
Объявите класс GeyserClassic - фильтр для очистки воды. В этом классе должно быть три слота для фильтров. Каждый слот строго для своего класса фильтра:
Mechanical - для очистки от крупных механических частиц;
Aragon - для последующей очистки воды;
Calcium - для обработки воды на третьем этапе.
Объекты классов фильтров должны создаваться командами:
filter_1 = Mechanical(дата установки)
filter_2 = Aragon(дата установки)
filter_3 = Calcium(дата установки)
Во всех объектах этих классов должен формироваться локальный атрибут:
date - дата установки фильтров (для простоты - положительное вещественное число).
Также нужно запретить изменение этого атрибута после создания объектов этих классов (только чтение). В случае присвоения нового значения, прежнее значение не менять. Ошибок никаких не генерировать.
Объекты класса GeyserClassic должны создаваться командой:
g = GeyserClassic()
А сам класс иметь атрибут:
MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого) и следующие методы:
add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3), если он (слот) пустой (без фильтра). Также здесь следует проверять, что в первый слот можно установить только объекты класса Mechanical, во второй - объекты класса Aragon и в третий - объекты класса Calcium. Иначе слот должен оставаться пустым.
remove_filter(self, slot_num) - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);
get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);
water_on(self) - включение воды: возвращает True, если вода течет и False - в противном случае.
Метод water_on() должен возвращать значение True при выполнении следующих условий:
- все три фильтра установлены в слотах;
- все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])
Пример использования классов  (эти строчки в программе писать не нужно):
my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
P.S. На экран ничего выводить не нужно.
"""

import time
from typing import Dict, Optional, Type


class BaseFilter:

    def __init__(self, date: float):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key not in self.__dict__:
            if isinstance(value, float) and value > 0:
                super().__setattr__(key, value)
        elif key != 'date':
            super().__setattr__(key, value)


class Mechanical(BaseFilter):
    def __init__(self, date: float):
        super().__init__(date)


class Aragon(BaseFilter):

    def __init__(self, date: float):
        super().__init__(date)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)


class Calcium(BaseFilter):

    def __init__(self, date: float):
        super().__init__(date)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)


class GeyserClassic:

    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots: Dict[int, Optional[BaseFilter]] = {
            1: None,
            2: None,
            3: None,
        }
        self.filter_types: Dict[int, Type[BaseFilter]] = {
            1: Mechanical,
            2: Aragon,
            3: Calcium,
        }

    def __check_filter_type(self, slot_num: int, fltr: BaseFilter) -> bool:
        return isinstance(fltr, self.filter_types.get(slot_num, BaseFilter))

    def __check_slots(self, slot_num: int, fltr: BaseFilter) -> bool:
        return slot_num in self.slots and self.slots[slot_num] is None and isinstance(fltr, BaseFilter)

    def __check_installed_filters(self) -> bool:
        return all(self.slots.values())

    def __check_filter_life(self) -> bool:
        current_time = time.time()
        return all(0 <= current_time - fltr.date <= self.MAX_DATE_FILTER for fltr in self.slots.values() if fltr is not None)

    def add_filter(self, slot_num: int, fltr: BaseFilter) -> None:
        if self.__check_slots(slot_num, fltr):
            if self.__check_filter_type(slot_num, fltr):
                self.slots[slot_num] = fltr

    def remove_filter(self, slot_num: int) -> None:
        if slot_num in self.slots:
            self.slots[slot_num] = None

    def get_filters(self) -> tuple:
        return tuple(self.slots.values())

    def water_on(self) -> bool:
        return self.__check_installed_filters() and self.__check_filter_life()

