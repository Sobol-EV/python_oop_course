"""
Объявите в программе следующие несколько классов:
CPU - класс для описания процессоров;
Memory - класс для описания памяти;
MotherBoard - класс для описания материнских плат.
Обеспечить возможность создания объектов каждого класса командами:
cpu = CPU(наименование, тактовая частота)
mem = Memory(наименование, размер памяти)
mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Memory, максимум N - по числу слотов памяти на материнской плате (N = 4).
Объекты классов должны иметь следующие локальные свойства:
для класса CPU: name - наименование; fr - тактовая частота;
для класса Memory: name - наименование; volume - объем памяти;
для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется);
mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти).
Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов на материнской плате в виде следующего списка из четырех строк:
['Материнская плата: <наименование>',
'Центральный процессор: <наименование>, <тактовая частота>',
'Слотов памяти: <общее число слотов памяти>',
'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']
Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).
P.S. Отображать на экране ничего не нужно, только создать объект по указанным требованиям.
"""

class Component:
    def __init__(self, name):
        self.name = name

    def get_description(self):
        raise NotImplementedError


class CPU(Component):
    def __init__(self, name, fr):
        super().__init__(name)
        self.fr = fr

    def get_description(self):
        return f"{self.name}, {self.fr}"


class Memory(Component):
    def __init__(self, name, volume):
        super().__init__(name)
        self.volume = volume

    def get_description(self):
        return f"{self.name} - {self.volume}"


class MotherBoard:
    total_mem_slots = 4

    def __init__(self, name, cpu: CPU, *mem_slots: Memory):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots[:self.total_mem_slots]

    def get_motherboard_info(self):
        return f"Материнская плата: {self.name}"

    def get_cpu_info(self):
        return f"Центральный процессор: {self.cpu.get_description()}"

    def get_memory_slots_info(self):
        return f"Слотов памяти: {self.total_mem_slots}"

    def get_memory_info(self):
        return "Память: " + "; ".join(mem.get_description() for mem in self.mem_slots)

    def get_config(self):
        return [
            self.get_motherboard_info(),
            self.get_cpu_info(),
            self.get_memory_slots_info(),
            self.get_memory_info()
        ]


cpu = CPU("Intel Core i7", "3.8")
mem1 = Memory("Kingston", "8")
mem2 = Memory("Corsair", "16")
mb = MotherBoard("ASUS Prime", cpu, mem1, mem2)

