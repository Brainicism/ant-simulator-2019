from peewee import *
from .base_model import BaseModel

class Users(BaseModel):
    discord_id = CharField()
    server_id = CharField()

    class Meta:
        primary_key = CompositeKey('discord_id', 'server_id')
        constraints = [SQL("UNIQUE(discord_id, server_id)")]
