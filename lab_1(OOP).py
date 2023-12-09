# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Product:
    def __init__(self, name: str, price: float):
        '''
        Создание и подготовка к работе объект "Продукт"

        :param name: Назвение продукта
        :param price: Цена продукта

        Примеры:
        >>> carrot = Product('carrot', 29.99)
        '''

        self.name = name
        if not isinstance(price, (int, float)):
            raise TypeError('Цена может быть только int or float')
        if price < 0:
            raise ValueError('Цена не может быть отрицательной')
        self.price = price


class User:
    def __init__(self, login: str, value: (int, float) = 0):
        '''
        Создание и подготовка к работе объект "Пользователь"

        :param login: Логин прользователя
        :param value: Количество денег на балансе

        Примеры:
        >>> user1 = User('svyatoy_tapok')
        >>> user2 = User('baratrum', 100)
        '''

        self.login = login
        if not isinstance(value, (int, float)):
            raise TypeError('Баланс может быть только int or float')
        if value < 0:
            raise ValueError('Баланс не может быть отрицательным')
        self.balance = value

    @property
    def balance(self):
        '''
        Проверка баланса, getter

        Примеры:
        >>> user2 = User('svyatoy_tapok', 100)
        >>> user2.balance
        100
        '''
        return self.__balance

    @balance.setter
    def balance(self, value: (int, float)):
        '''
        Установка баланса, setter

        :param value: значение баланса

        Примеры:
        >>> user2 = User('svyatoy_tapok')
        >>> user2.balance(99)
        '''
        if value < 0:
            raise ValueError('Баланс не может быть отрицательным')
        self.__balance = value

    def deposit(self, value: (int, float)):
        '''
        Пополнение баланса

        :param value: значение для пополнения баланса

        Примеры:
        >>> user2 = User('svyatoy_tapok', 100)
        >>> user2.deposit(10)
        >>> user2.balance
        110
        '''

        if value < 0:
            raise ValueError('Отрицательное значение недопустимо')
        self.__balance += value

    def payment(self, value: (int, float)):
        '''
        Оплата товаров

        :param value: значение для списания с баланса

        Примеры:
        >>> user2 = User('svyatoy_tapok', 100)
        >>> user2.payment(90)
        True
        >>> user2.payment(11)
        Не хватает средств на балансе. Пополните счет
        '''
        if value < 0:
            raise ValueError('Отрицательное значение недопустимо')
        if self.balance < value:
            print(f'Не хватает средств на балансе. Пополните счет')
        else:
            self.balance -= value
            return True


class Cart:
    def __init__(self, user: User):
        '''
        Создание и подготовка к работе объект "Корзина"

        :param user: пользователь - экземпляр класса User

        Примеры:
        >>> user1 = User('svyatoy_tapok')
        >>> cart_user1 = Cart(user1)
        '''
        if isinstance(user, User):
            self.user = user
        else: TypeError('user должен быть объектом "Пользователь"')
        self.goods = {}
        self.__total = 0

    def add(self, product: Product, value: int = 1):
        '''
        Добавляет продукт и его количество в корзину пользователя

        :param product: продукт - экземпляр класса Product
        :param value: количество продукта

        Примеры:
        >>> user1 = User('svyatoy_tapok')
        >>> carrot = Product('carrot', 29)
        >>> cart_user1 = Cart(user1)
        >>> cart_user1.add(carrot)
        '''
        if not isinstance(value, int):
            raise TypeError('Количество может быть только int')
        if value < 0:
            raise ValueError('Количество не может быть отрицательным')
        pass


    def remove(self, product: Product, value: int = 1):
        '''
        Удаляет продукт или его количество из корзины пользователя

        :param product: продукт - экземпляр класса Product
        :param value: количество продукта

        Примеры:
        >>> user1 = User('svyatoy_tapok')
        >>> carrot = Product('carrot', 29)
        >>> cart_user1 = Cart(user1)
        >>> cart_user1.add(carrot, 3)
        >>> cart_user1.remove(carrot, 2)
        '''
        if not isinstance(value, int):
            raise TypeError('Количество может быть только int')
        if value < 0:
            raise ValueError('Количество не может быть отрицательным')
        pass


if __name__ == "__main__":
    doctest.testmod()
