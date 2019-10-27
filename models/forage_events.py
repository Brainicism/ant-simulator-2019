from peewee import *
from .base_model import BaseModel

class Forage_events(BaseModel):
    event_description = CharField()
    event_rarity = CharField()
