import datetime
from peewee import *
from .colony import Colony
from .base_model import BaseModel

class Ants(BaseModel):
    colony_id = ForeignKeyField(Colony, on_delete='CASCADE')
    name = CharField()
    role = CharField()
    life_stage = IntegerField()
    birth_date = DateTimeField(default=datetime.datetime.now)
