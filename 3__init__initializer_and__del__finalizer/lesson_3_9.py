"""Объявите два класса:

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)
Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие/отсутствие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).

<ИЗОБРАЖЕНИЕ lesson_3_9.jpeg>

С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается символ #; мина отображается символом *; между клетками при отображении ставить пробел).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.

P.S. На экран в программе ничего выводить не нужно."""

import random


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.size_pole = N
        self.count_mine = M
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]
        self.init()

    def init(self):
        self._lay_mines()
        self._count_mines()

    def _lay_mines(self):
        placed_mines = 0
        while placed_mines < self.count_mine:
            x, y = random.randint(0, self.size_pole - 1), random.randint(0, self.size_pole - 1)
            if not self.pole[x][y].mine:
                self.pole[x][y].mine = True
                placed_mines += 1

    def _count_mines(self):
        for i in range(self.size_pole):
            for j in range(self.size_pole):
                if not self.pole[i][j].mine:
                    self.pole[i][j].around_mines = sum(
                        self.pole[x][y].mine
                        for x in range(max(0, i-1), min(i+2, self.size_pole))
                        for y in range(max(0, j-1), min(j+2, self.size_pole))
                        if (x, y) != (i, j)
                    )

    def show(self):
        for i in range(self.size_pole):
            for j in range(self.size_pole):
                cell = self.pole[i][j]
                if cell.fl_open:
                    print('*' if cell.mine else cell.around_mines, end=" ")
                else:
                    print('#', end=" ")
            print()


pole_game = GamePole(10, 12)

