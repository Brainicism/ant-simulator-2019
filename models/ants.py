from peewee import *
from .colony import Colony
from .base_model import BaseModel

class Ants(BaseModel):
    colony_id = ForeignKeyField(Colony, to_field="id")
    name = CharField()
    life_stage = CharField()
    birth_date = DateTimeField()
