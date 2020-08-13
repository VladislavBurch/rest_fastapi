from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str


class ProductCreate(ProductBase):
    description: str


class Product(ProductBase):
    id: int
    is_available: bool
    description: str

    class Config:
        orm_mode = True
