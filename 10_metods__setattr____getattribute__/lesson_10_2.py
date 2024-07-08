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
