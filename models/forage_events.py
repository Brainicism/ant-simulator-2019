from peewee import *
from .base_model import BaseModel

class ForageEvents(BaseModel):
    event_description = CharField()
    event_rarity = IntegerField()
    event_death_multiplier = FloatField()
    event_food_multiplier = FloatField()
    image_url = CharField()