"""
Объявите в программе класс Cart (корзина), объекты которого создаются командой:
cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.
В классе Cart объявить методы:
add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:
['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']
Объявите в программе следующие классы для описания товаров:
Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.
Объекты этих классов должны создаваться командой:
gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:
name - наименование;
price - цена.
Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.
P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.
"""


class Product:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name_and_price(self) -> str:
        return f"{self.name}: {self.price}"


class Table(Product):

    def __init__(self, name: str, price: float):
        super().__init__(name, price)


class TV(Product):

    def __init__(self, name: str, price: float):
        super().__init__(name, price)


class Notebook(Product):

    def __init__(self, name: str, price: float):
        super().__init__(name, price)


class Cup(Product):

    def __init__(self, name: str, price: float):
        super().__init__(name, price)


class Cart:

    def __init__(self):
        self.goods = []

    def add(self, gd: Product):
        self.goods.append(gd)

    def remove(self, indx: int):
        self.goods.pop(indx)

    def get_list(self):
        return [good.get_name_and_price() for good in self.goods]


cart = Cart()

cart.add(TV("LG", 100))
cart.add(TV("LG", 100))
cart.add(Table("LG", 100))
cart.add(Notebook("LG", 100))
cart.add(Notebook("LG", 100))
cart.add(Cup("LG", 100))

