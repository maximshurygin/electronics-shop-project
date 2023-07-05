import csv
from pathlib import Path
from src.error import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)

    def __repr__(self):
        """возвращает описание для разработчика"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """возвращает описание для пользователя"""
        return self.name

    def __add__(self, other):
        """возвращает сумму количества товаров или TypeError"""
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @staticmethod
    def string_to_number(string):
        """статический метод, возвращающий число из числа-строки"""
        return int(float(string))

    @classmethod
    def instantiate_from_csv(cls):
        """инициализирует экземпляры класса Item данными из CSV-файла."""
        cls.all = []

        project_dir = Path(__file__).resolve().parent
        file_path = project_dir / 'items.csv'
        try:
            with open(file_path, 'r', encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError
                    name = row['name']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return int(self.price * self.quantity * self.__class__.pay_rate)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.__class__.pay_rate
