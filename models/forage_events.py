from peewee import *
from .base_model import BaseModel

class ForageEvents(BaseModel):
    event_description = CharField()
    event_rarity = IntegerField()