import json
import os
from typing import List

from pydantic import BaseModel

from models.product import Product, ProductOrder, CustomBaseModel, ListProduct


def get_data(path: str, model: CustomBaseModel):
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


def get_data_json(path: str):
    data = []
    if not os.path.exists(path):
        print('Не валидный путь до файла')
        return data
    return ListProduct.parse_file(path)


def get_product(path: str) -> List[Product]:
    """
    Получение продуктов
    :param path: Путь до файла продуктов
    :return: Данные продуктов
    """
    return get_data(path, ProductOrder)


def get_price(path: str) -> List[ProductOrder]:
    return get_data_json(path)
