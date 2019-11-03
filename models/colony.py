from peewee import *
from .users import Users
from .species import Species
from .base_model import BaseModel

class Colony(BaseModel):
    user = ForeignKeyField(Users, on_delete="CASCADE")
    species = ForeignKeyField(Species, to_field="id")
    colony_name = CharField()
    current_food_supply = IntegerField()
    max_food_supply = IntegerField()
