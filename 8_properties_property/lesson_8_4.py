"""
 Объявите класс RadiusVector2D, объекты которого должны создаваться командами:

v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
В каждом объекте класса RadiusVector2D должны формироваться локальные приватные атрибуты:

__x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).

В классе RadiusVector2D необходимо объявить два объекта-свойства:

x - для изменения и считывания локального атрибута __x;
y - для изменения и считывания локального атрибута __y.

При инициализации и изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:

- значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].

Если проверка не проходит, то координаты не меняются (напомню, что при инициализации они изначально равны 0). Величины MIN_COORD = -100, MAX_COORD = 1024 задаются как публичные атрибуты класса RadiusVector2D.

Также в классе RadiusVector2D необходимо объявить статический метод:

norm2(vector) - для вычисления квадратической нормы vector - переданного объекта класса RadiusVector2D (квадратическая норма вектора: x*x + y*y).

P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""


class RadiusVector2D:

    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @classmethod
    def check_value(cls, value):
        return (isinstance(value, int) or isinstance(value, float)) and (cls.MIN_COORD <= value <= cls.MAX_COORD)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.check_value(x):
            self.__x = x
        else:
            if not hasattr(self, 'x'):
                self.__x = 0

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.check_value(y):
            self.__y = y
        else:
            if not hasattr(self, 'y'):
                self.__y = 0

    @staticmethod
    def norm2(vector):
        if isinstance(vector, RadiusVector2D):
            x = vector.x
            y = vector.y
            return x**2 + y**2

