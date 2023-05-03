import os
from typing import List, Any

from models.product import ProductOrder, ListProduct


def get_data(path: str, model: Any) -> list:
    """
    Получение данных из файла и сериализация из в модели
    :param path: Путь до файла
    :param model: Модель для сериализации
    :return:
    """
    data = []
    if not os.path.exists(path):
        print('Не валидный путь до файла')
        return data
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            if line:
                info = line.split(' ')
                data.append(model(**dict(zip(model.get_name_fields(), info))))
    return data


def get_data_json(path: str, model: Any) -> ListProduct:
    """
    Получение данных из json-файла
    :param path: Путь до json файла
    :param model: Модель для сериализации данных
    :return:
    """
    if not os.path.exists(path):
        raise FileNotFoundError('Не найден путь до файла')
    return model.parse_file(path)


def get_product(path: str) -> List[ProductOrder]:
    """
    Получение продуктов
    :param path: Путь до файла продуктов
    :return: Данные продуктов
    """
    return get_data(path, ProductOrder)


def get_price(path: str) -> ListProduct:
    """
    Получение стоимости товар
    :param path: Путь до файла с ценами
    :return: Сериализованные данные словаря цен
    """
    return get_data_json(path, ListProduct)
