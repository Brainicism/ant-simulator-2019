from peewee import *
from .base_model import BaseModel

class Species(BaseModel):
    species_name = CharField()
    image_url = CharField()
    hp_multiplier = DoubleField()
    strength_multiplier = DoubleField()
    forage_multiplier = DoubleField()
