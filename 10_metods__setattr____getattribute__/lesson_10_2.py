"""
Вы создаете интернет-магазин. Для этого нужно объявить два класса:

Shop - класс для управления магазином в целом;
Product - класс для представления отдельного товара.

Объекты класса Shop следует создавать командой:

shop = Shop(название магазина)
В каждом объекте класса Shop должно создаваться локальное свойство:

goods - список товаров (изначально список пустой).

А также в классе объявить методы:

add_product(self, product) - добавление нового товара в магазин (в конец списка goods);
remove_product(self, product) - удаление товара product из магазина (из списка goods);

Объекты класса Product следует создавать командой:

p = Product(название, вес, цена)
В них автоматически должны формироваться локальные атрибуты:

id - уникальный идентификационный номер товара (генерируется автоматически как целое положительное число от 1 и далее);
name - название товара (строка);
weight - вес товара (целое или вещественное положительное число);
price - цена (целое или вещественное положительное число).

В классе Product через магические методы (подумайте какие) осуществить проверку на тип присваиваемых данных локальным атрибутам объектов класса (например, id - целое число, name - строка и т.п.). Если проверка не проходит, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
Также в классе Product с помощью магического(их) метода(ов) запретить удаление локального атрибута id. При попытке это сделать генерировать исключение:

raise AttributeError("Атрибут id удалять запрещено.")
Пример использования классов (в программе эти строчки не писать):

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
P.S. На экран ничего выводить не нужно.
"""
class Product:
    __id_counter = 1

    __valid_types = {
        "id": int,
        "name": str,
        "weight": (int, float),
        "price": (int, float),
    }

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.id = cls.__id_counter
        cls.__id_counter += 1
        return instance

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in self.__valid_types:
            if (not isinstance(value, self.__valid_types[key]) or
                    (key in ["weight", "price"] and value <= 0)):
                raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

    def __delattr__(self, key):
        if key == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(key)


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)
