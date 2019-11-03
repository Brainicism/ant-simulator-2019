from peewee import *
from .base_model import BaseModel

class Shop_items(BaseModel):
    name = CharField()
    description = CharField()
    price = IntegerField()
