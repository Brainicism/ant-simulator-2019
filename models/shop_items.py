from peewee import *
from .base_model import BaseModel

class ShopItems(BaseModel):
    name = CharField()
    description = CharField()
    price = IntegerField()
