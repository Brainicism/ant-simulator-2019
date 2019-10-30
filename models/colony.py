from peewee import *
from .users import Users
from .species import Species
from .base_model import BaseModel

class Colony(BaseModel):
    discord_id = ForeignKeyField(Users, to_field="discord_id", on_delete="CASCADE")
    server_id = ForeignKeyField(Users, to_field="server_id",  on_delete="CASCADE")
    species_id = ForeignKeyField(Species, to_field="id")
    colony_name = CharField()
