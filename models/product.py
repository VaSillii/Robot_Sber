from typing import List

from pydantic import BaseModel


class CustomBaseModel(BaseModel):
    """
    Базовая кастомная модель
    """
    @classmethod
    def get_name_fields(cls):
        return cls.__fields__.keys()


class Product(CustomBaseModel):
    """
    Модель описания продукта
    """
    full_name: str
    price: int

    class Config:
        schema_extra = {
            'example': {
                'full_name': 'Пискаревский МЗ',
                'price': 123,
            }
        }


class Category(CustomBaseModel):
    """
    Модель описания категории
    """
    short_name: str
    variants: List[Product]

    class Config:
        schema_extra = {
            'example': {
                'short_name': 'молоко',
                'variants': [
                    {
                        'full_name': 'Пискаревский МЗ',
                        'price': 123,
                    }
                ],
            }
        }


class ListProduct(CustomBaseModel):
    """
    Модель опивания Списка продуктов
    """
    data: List[Category]

    class Config:
        schema_extra = {
            'example': {
                'data': [
                    {
                        'short_name': 'молоко',
                        'variants': [
                            {
                                'full_name': 'Пискаревский МЗ',
                                'price': 123,
                            }
                        ],
                    }
                ]
            }
        }


class ProductOrder(CustomBaseModel):
    """
    Модель продукта:
        * name - наименование продукта
        * cnt - количество товара
    """
    name: str
    cnt: int

    class Config:
        schema_extra = {
            'example': {
                'name': 'Молоко',
                'cnt': 1,
            }
        }
