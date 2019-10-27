from peewee import *
from .colony import Colony
from .base_model import BaseModel

class Ants(BaseModel):
    colony_id = ForeignKeyField(Colony, to_field="id")
    name = CharField()
    type = CharField()
    life_stage = IntegerField()
    birth_date = DateTimeField()
