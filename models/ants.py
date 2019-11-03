import datetime
from peewee import *
from .colony import Colony
from .base_model import BaseModel

class Ants(BaseModel):
    colony = ForeignKeyField(Colony, on_delete="CASCADE", backref="ants")
    name = CharField()
    role = IntegerField()
    life_stage = IntegerField()
    birth_date = DateTimeField(default=datetime.datetime.now)
