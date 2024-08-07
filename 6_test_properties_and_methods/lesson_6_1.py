"""
Представьте, что вы получили задание от заказчика. Вас просят реализовать простую имитацию локальной сети, состоящую
из набора серверов, соединенных между собой через роутер.

<ИЗОБРАЖЕНИЕ lesson_6_1.json>

Каждый сервер может отправлять пакет любому другому серверу сети. Для этого у каждого есть свой уникальный IP-адрес.
Для простоты - это просто целое (натуральное) число от 1 и до N, где N - общее число серверов. Алгоритм следующий. Предположим, сервер с IP = 2 собирается отправить пакет информации серверу с IP = 3. Для этого, он сначала отправляет пакет роутеру, а уже тот, смотрит на IP-адрес и пересылает пакет нужному узлу (серверу).

Для реализации этой схемы программе предлагается объявить три класса:

Server - для описания работы серверов в сети;
Router - для описания работы роутеров в сети (в данной задаче полагается один роутер);
Data - для описания пакета информации.

Серверы будут создаваться командой:

sv = Server()
При этом, уникальный IP-адрес каждого сервера должен формироваться автоматически при создании нового экземпляра класса Server.

Далее, роутер должен создаваться аналогичной командой:

router = Router()
А, пакеты данных, командой:

data = Data(строка с данными, IP-адрес назначения)
Для формирования и функционирования локальной сети, в классе Router должны быть реализованы следующие методы:

link(server) - для присоединения сервера server (объекта класса Server) к роутеру (для простоты, каждый сервер соединен
только с одним роутером);
unlink(server) - для отсоединения сервера server (объекта класса Server) от роутера;
send_data() - для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам
(после отправки буфер должен очищаться).

И одно обязательное локальное свойство (могут быть и другие свойства):

buffer - список для хранения принятых от серверов пакетов (объектов класса Data).

Класс Server должен содержать свой набор методов:

send_data(data) - для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
(пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
get_data() - возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список) и очищает входной буфер;
get_ip() - возвращает свой IP-адрес.

Соответственно в объектах класса Server должны быть локальные свойства:

buffer - список принятых пакетов (объекты класса Data, изначально пустой);
ip - IP-адрес текущего сервера.

Наконец, объекты класса Data должны содержать два следующих локальных свойства:

data - передаваемые данные (строка);
ip - IP-адрес назначения.

Пример использования этих классов (эти строчки в программе писать не нужно):

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

Ваша задача реализовать классы Router, Server и Data в соответствии с приведенным техническим заданием (ТЗ).
Что-либо выводить на экран не нужно.
"""

from typing import Dict, List


class Data:

    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Server:

    ip_gen = 0

    def __new__(cls, *args, **kwargs):
        cls.ip_gen += 1
        return super().__new__(cls)

    def __init__(self):
        self.buffer: List[Data] = []
        self.link_router = None
        self.ip = self.ip_gen

    def send_data(self, data: Data):
        self.link_router.buffer.append(data)

    def get_data(self):
        data_to_return = self.buffer[:]
        self.buffer.clear()
        return data_to_return

    def get_ip(self):
        return self.ip


class Router:

    connected_servers: Dict[int, Server] = {}
    buffer: List[Data] = []

    def link(self, server: Server):
        self.connected_servers[server.ip] = server
        server.link_router = self

    def unlink(self, server: Server):
        self.connected_servers.pop(server.ip)
        server.link_router = None

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.connected_servers:
                self.connected_servers[data.ip].buffer.append(data)
        self.buffer.clear()

