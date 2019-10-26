from peewee import *
from .base_model import BaseModel

class Colony(BaseModel):
    user_id = CharField()
    colony_name = CharField()