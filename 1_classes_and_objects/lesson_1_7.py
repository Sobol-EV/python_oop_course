"""
Объявите класс с именем Figure и двумя атрибутами:

type_fig: 'ellipse'
color: 'red'
Создайте экземпляр с именем fig1 этого класса и добавьте в него следующие локальные атрибуты:

start_pt: (10, 5)
end_pt: (100, 20)
color: 'blue'
Удалите из экземпляра класса свойство color и выведите на экран список всех локальных свойств (без значений) объекта
fig1 в одну строчку через пробел в порядке, указанном в задании.
"""


class Figure:
    type_fig = 'ellipse'
    color = 'red'

    def __init__(self):
        self.start_pt = None
        self.end_pt = None

    def add_attribute(self, attr_name, value):
        setattr(self, attr_name, value)

    def remove_attribute(self, attr_name):
        if hasattr(self, attr_name):
            delattr(self, attr_name)

    def list_attributes(self):
        return vars(self).keys()


fig1 = Figure()

fig1.add_attribute('start_pt', (10, 5))
fig1.add_attribute('end_pt', (100, 20))
fig1.add_attribute('color', 'blue')

fig1.remove_attribute('color')

print(" ".join(fig1.list_attributes()))

