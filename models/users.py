from peewee import *
from .base_model import BaseModel

class Users(BaseModel):
    discord_id = CharField()
    server_id = CharField()
