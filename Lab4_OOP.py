
class Vehicle:
    """Базовый класс для транспортных средств."""

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация объекта Vehicle.

        :param brand: Бренд ТС.
        :param model: Модель ТС.
        :param year: Год выпуска ТС.
        """

        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление ТС."""
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """Возвращает подробное строковое представление ТС."""
        return f"Vehicle(brand={self.brand}, model={self.model}, year={self.year})"

    def move(self, distance: float) -> str:
        """
        Перемещение ТС на заданное расстояние.

        :param distance: Расстояние, на которое нужно переместить автомобиль.
        """

        return f"Транспортное средство [{self.brand} {self.model} ({self.year})] прошло {distance} километров."

    def refuel(self) -> str:
        """
        Заправка ТС
        """
        return "ТС было заправлено"

class Car(Vehicle):
    """Класс, представляющий автомобиль, наследующий от Vehicle."""

    def __init__(self, brand: str, model: str, year: int, passengers: int):
        """
        Инициализация объекта Car.

        :param brand: Бренд автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        super().__init__(brand, model, year)
        self.passengers = passengers

    def __str__(self) -> str:
        """Возвращает строковое представление автомобиля."""
        return f"{super().__str__()}, Пассажиры: {self.passengers}"

    def __repr__(self) -> str:
        """Возвращает подробное строковое представление автомобиля."""
        return f"Car(brand={self.brand}, model={self.model}, year={self.year}, passengers={self.passengers})"

    def start_engine(self) -> str:
        """
        Запустить двигатель автомобиля.
        """
        return "Двигатель успешно запустился."

    def honk(self) -> str:
        """
        Издает звук клаксона автомобиля.
        """
        return "Beep Beep!"

    def move(self, distance: float) -> str:
        """
        Перемещение для автомобиля
        (а не для самолета, например)

        :param distance: Расстояние, на которое нужно переместить автомобиль.
        """
        return f"Транспортное средство [{self.brand} {self.model} ({self.year}) {self.passengers} пассажиров] прошло {distance} километров."


if __name__ == "__main__":
    vehicle = Vehicle("Toyota", "Camry", 2022)
    print(vehicle.move(50))
    print(vehicle.refuel())

    car = Car("Honda", "Accord", 2020, 5)
    print(car.move(50))
    print(car.refuel())
    print(car.honk())



