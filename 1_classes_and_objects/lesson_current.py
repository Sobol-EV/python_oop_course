class Book:

    def __init__(self, name: str = "", autor: str = "", pages: int = 0, year: int = 0):
        self.name = name
        self.autor = autor
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        is_true = False
        if key in ["name", "autor", "pages", "year"]:
            if (key == "name") and (isinstance(value, str)):
                is_true = True
            if key == "autor" and (isinstance(value, str)):
                is_true = True
            if key == "pages" and (isinstance(value, int)):
                is_true = True
            if key == "year" and (isinstance(value, int)):
                is_true = True
            if is_true:
                return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

book = Book("Python ООП", "Сергей Балакирев", 123, 2022)