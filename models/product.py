from typing import List

from pydantic import BaseModel


class CustomBaseModel(BaseModel):
    @classmethod
    def get_name_fields(cls):
        return cls.__fields__.keys()


class Product(CustomBaseModel):
    full_name: str
    price: int


class Category(CustomBaseModel):
    short_name: str
    variants: List[Product]


class ListProduct(CustomBaseModel):
    data: List[Category]


class ProductOrder(CustomBaseModel):
    """
    Модель продукта:
        * name - наименование продукта
        * cnt - количество товара
    """
    name: str
    cnt: int


