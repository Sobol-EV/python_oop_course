"""
Вам требуется сформировать класс PathLines для описания маршрутов, состоящих из линейных сегментов. При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo. Объекты этого класса будут формироваться командой:

line = LineTo(x, y)
где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).

В каждом объекте класса LineTo должны формироваться локальные атрибуты:

x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).

Объекты класса PathLines должны создаваться командами:

p = PathLines()                   # начало маршрута из точки 0, 0
p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
где line1, line2, ... - объекты класса LineTo.

Сам же класс PathLines должен иметь следующие методы:

get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.

Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента определяется как евклидовое расстояние по формуле:

L = sqrt((x1-x0)^2 + (y1-y0)^2)

где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.

Пример использования классов (эти строчки в программе писать не нужно):

p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""

from math import sqrt


class LineTo:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class PathLines:

    def __init__(self, *args: LineTo):
        self.path_l = [*args]

    @staticmethod
    def formula(x0, y0, x1, y1):
        return sqrt((x1-x0)**2 + (y1-y0)**2)

    def get_path(self):
        return self.path_l

    def get_length(self):
        sum_l = 0
        for i, _ in enumerate(self.path_l):
            if i:
                sum_l += self.formula(self.path_l[i-1].x, self.path_l[i-1].y, self.path_l[i].x, self.path_l[i].y)
            else:
                sum_l += self.formula(0, 0, self.path_l[i].x, self.path_l[i].y)
        return sum_l

    def add_line(self, line: LineTo):
        self.path_l.append(line)
