"""
Объявите класс с именем TravelBlog и объявите в нем атрибут:

total_blogs: 0
Создайте экземпляр этого класса с именем tb1, сформируйте в нем два локальных свойства:

name: 'Франция'
days: 6
Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.

Создайте еще один экземпляр класса TravelBlog с именем tb2, сформируйте в нем два локальных свойства:

name: 'Италия'
days: 5
Увеличьте значение атрибута total_blogs класса TravelBlog еще на единицу.

P.S. На экран ничего выводить не нужно.
"""


class TravelBlog:
    total_blogs = 0

    def __init__(self, name, days):
        self.name = name
        self.days = days
        TravelBlog.total_blogs += 1


tb1 = TravelBlog("Франция", 6)
tb2 = TravelBlog("Италия", 5)

