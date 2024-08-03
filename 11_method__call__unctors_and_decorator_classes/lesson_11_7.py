"""
Необходимо объявить класс-декоратор с именем Handler, который можно было бы применять к функциям следующим образом:
@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"
Здесь аргумент methods декоратора Handler содержит список разрешенных запросов для обработки. Сама декорированная функция вызывается по аналогии с предыдущим подвигом:
res = contact({"method": "POST", "url": "contact.html"})
В результате функция contact должна возвращать строку в формате:

"<метод>: <данные из функции>"

В нашем примере - это будет:

"POST: Сергей Балакирев"

Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос. Если ключ method принимает значение отсутствующее в списке methods декоратора Handler, например, "PUT", то декорированная функция contact должна возвращать значение None.
Для имитации GET и POST-запросов в классе Handler необходимо объявить два вспомогательных метода с сигнатурами:

def get(self, func, request, *args, **kwargs) - для имитации обработки GET-запроса
def post(self, func, request, *args, **kwargs) - для имитации обработки POST-запроса

В зависимости от типа запроса должен вызываться соответствующий метод (его выбор в классе можно реализовать методом __getattribute__()). На выходе эти методы должны формировать строки в заданном формате.
P.S. В программе достаточно объявить только класс. Ничего на экран выводить не нужно.
"""

from typing import Callable, Dict, Any, List


class General:
    def __init__(self, func: Callable):
        self.__func = func

    def __call__(self, func: Callable, request: Dict[str, Any], *args: Any, **kwargs: Any) -> str:
        method = request.get('method', 'GET')
        return f'{method}: {func(request, *args, **kwargs)}'

class Handler:
    def __init__(self, methods: List[str]):
        self.__methods = methods

    def __call__(self, func: Callable):
        def wrapper(request: Dict[str, Any], *args: Any, **kwargs: Any) -> Any:
            method = request.get('method', 'GET')
            if method in self.__methods:
                if method == 'GET':
                    return self.get(func, request, *args, **kwargs)
                elif method == 'POST':
                    return self.post(func, request, *args, **kwargs)
            return None
        return wrapper

    @General
    def get(self, request: Dict[str, Any], *args: Any, **kwargs: Any) -> Any:
        return "Processed GET request"

    @General
    def post(self, request: Dict[str, Any], *args: Any, **kwargs: Any) -> Any:
        return "Processed POST request"

