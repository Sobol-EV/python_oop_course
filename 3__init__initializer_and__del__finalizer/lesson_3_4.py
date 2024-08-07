"""
Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:
tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.
В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:
1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.
Проверку параметров a, b, c проводить именно в таком порядке.
Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:
a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c.
Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).
Sample Input: 3 4 5
Sample Output: 3
"""


class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __validation_input(element):
        if (type(element) == int or type(element) == float) and (element > 0):
            return True
        return False

    def is_triangle(self):
        if self.__validation_input(self.a) and \
                self.__validation_input(self.b) and \
                self.__validation_input(self.c):
            if (self.a + self.b) > self.c and \
                    (self.b + self.c) > self.a and \
                    (self.c + self.a) > self.b:
                return 3  # Стороны образуют треугольник
            return 2  # Стороны не образуют треугольник
        return 1  # Неверный ввод


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

