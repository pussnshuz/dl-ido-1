
class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
    #Для rerp будет проблема со скобочками, поэтому для него я не применю наследование

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом.")
        if isinstance(value, bool):     #не самая важная проверка, но проверка выше допускает bool
            raise TypeError("Количество страниц не может быть булевым значением.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля.")
        self._pages = value

    def __str__(self):
        return super().__str__() + f'. Кол-во страниц: {self.pages}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: (int, float)):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Продолжительность должна быть числом.")
        if isinstance(value, bool):
            raise TypeError("Продолжительность не может быть булевым значением.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля.")
        self._duration = value

    def __str__(self):
        return super().__str__() + f'. Продолжительность: {self.duration}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"