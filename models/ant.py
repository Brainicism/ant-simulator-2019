from peewee import *
from .colony import Colony
from .base_model import BaseModel

class Ant(BaseModel):
    colony = ForeignKeyField(Colony, backref="ants", to_field="id")
    species = CharField()
    name = CharField()
    weight = IntegerField()
    power = IntegerField()
