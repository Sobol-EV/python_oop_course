"""
Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:
a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.
Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.
Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:
objs = [SingletonFive(str(n)) for n in range(10)]
P.S. В программе на экран ничего выводить не нужно.
"""


class SingletonFive:

    number_of_instances_created = 0
    reference_to_last_object = None
    last_args = None

    def __new__(cls, *args, **kwargs):

        if cls.number_of_instances_created < 5:
            cls.reference_to_last_object = super().__new__(cls)
            cls.last_args = args

        cls.number_of_instances_created += 1

        return cls.reference_to_last_object

    def __init__(self, name):
        self.name = name if self.number_of_instances_created < 5 else self.last_args[0]


objs = [SingletonFive(str(n)) for n in range(10)]

