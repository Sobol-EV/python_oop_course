"""
Объявите класс SmartPhone, объекты которого предполагается создавать командой:
sm = SmartPhone(марка смартфона)
Каждый объект должен содержать локальные атрибуты:
model - марка смартфона (строка);
apps - список из установленных приложений (изначально пустой).
Также в классе SmartPhone должны быть объявлены следующие методы:
add_app(self, app) - добавление нового приложения на смартфон (в конец списка apps);
remove_app(self, app) - удаление приложения по ссылке на объект app.
При добавлении нового приложения проверять, что оно отсутствует в списке apps (отсутствует объект соответствующего класса).
Каждое приложение должно определяться своим классом. Для примера объявите следующие классы:
AppVK - класс приложения ВКонтаке;
AppYouTube - класс приложения YouTube;
AppPhone - класс приложения телефона.
Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
app_1 = AppVK() # name = "ВКонтакте"
app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024
app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}) # name = "Phone", phone_list = словарь с контактами
Пример использования классов (в программе эти строчки не писать):
sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
P.S. На экран ничего выводить не нужно.
"""

from typing import Dict, List


class App:
    def __init__(self, name: str):
        self.name = name


class AppVK(App):
    def __init__(self):
        super().__init__("ВКонтакте")


class AppYouTube(App):
    def __init__(self, memory_max: int):
        super().__init__("YouTube")
        self.memory_max = memory_max


class AppPhone(App):
    def __init__(self, phone_list: Dict[str, int]):
        super().__init__("Phone")
        self.phone_list = phone_list


class SmartPhone:

    def __init__(self, model: str):
        self.model = model
        self.apps: List[App] = []
        self.app_types: set = set()

    def add_app(self, app: App):
        app_type = type(app)
        if app_type not in self.app_types:
            self.apps.append(app)
            self.app_types.add(app_type)

    def remove_app(self, app: App):
        app_type = type(app)
        if app in self.apps:
            self.apps.remove(app)
            if all(type(a) != app_type for a in self.apps):
                self.app_types.remove(app_type)

