"""
Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:
gr_1 = Graph(data)
где data - список из числовых данных (данные для графика). При создании каждого экземпляра класса должны формироваться следующие локальные свойства:
data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными, нужно создавать копию переданного списка);
is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);
В этом классе объявите следующие методы:
set_data(self, data) - для передачи нового списка данных в текущий график;
show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.
Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar() должны выводить сообщение:
"Отображение данных закрыто"
Прочитайте из входного потока числовые данные с помощью команды:
data_graph = list(map(int, input().split()))
Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(), затем метод set_show() со значением fl_show = False и вызовите метод show_table().
На экране должны отобразиться две соответствующие строки.
Sample Input:
8 11 10 -32 0 7 18
Sample Output:
Столбчатая диаграмма: 8 11 10 -32 0 7 18
Отображение данных закрыто
"""


class Graph:

    def __init__(self, data: list, is_show: bool = True):
        self.data = data.copy()
        self.is_show = is_show

    def _show_dec(func):
        def wrapper(self):
            if self.is_show:
                return func(self)
            else:
                print("Отображение данных закрыто")

        return wrapper

    def set_data(self, data: list):
        self.data = data.copy()

    @_show_dec
    def show_table(self):
        print(*self.data)

    @_show_dec
    def show_graph(self):
        print("Графическое отображение данных:", *self.data)

    @_show_dec
    def show_bar(self):
        print(f"Столбчатая диаграмма:", *self.data)

    def set_show(self, fl_show: bool):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)

gr.show_bar()
gr.set_show(False)
gr.show_table()

