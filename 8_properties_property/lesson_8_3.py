"""
Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов), когда один объект ссылается на следующий и так по цепочке до последнего:

<ИЗОБРАЖЕНИЕ lesson_8_3.jpeg>

Для этого объявите в программе два класса:

StackObj - для описания объектов односвязного списка;
Stack - для управления односвязным списком.

Объекты класса StackObj предполагается создавать командой:

obj = StackObj(данные)
Здесь данные - это строка с некоторым содержимым. Каждый объект класса StackObj должен иметь следующие локальные приватные атрибуты:

__data - ссылка на строку с данными, указанными при создании объекта;
__next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Также в классе StackObj должны быть объявлены объекты-свойства:

next - для записи и считывания информации из локального приватного свойства __next;
data - для записи и считывания информации из локального приватного свойства __data.

При записи необходимо реализовать проверку, что __next будет ссылаться на объект класса StackObj или значение None. Если проверка не проходит, то __next остается без изменений.

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта односвязного списка
В объектах класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого объекта в порядке их добавления, или пустой список, если объектов нет).

Пример использования классов Stack и StackObj (эти строчки в программе писать не нужно):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_obj: 'StackObj'):
        if isinstance(next_obj, StackObj) or next_obj is None:
            self.__next = next_obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj: StackObj):
        if self.tail is not None:
            self.tail.next = obj
            self.tail = obj

        if self.top is None:
            self.top = self.tail = obj

    def pop(self):
        last_temp = self.tail
        current = self.top
        if current is None:
            return None
        if current.next is None:
            self.tail = None
            self.top = None
            return last_temp
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.tail = current
        return last_temp

    def get_data(self):
        result = []
        current = self.top
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

