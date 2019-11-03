from peewee import *
from .users import Users
from .species import Species
from .base_model import BaseModel

class Colony(BaseModel):
    user_id = ForeignKeyField(Users, on_delete="CASCADE", backref="colonies")
    species_id = ForeignKeyField(Species, backref="colonies")
    colony_name = CharField()
    current_food_supply = IntegerField()
    max_food_supply = IntegerField()
