from peewee import *
from .users import Users
from .species import Species
from .base_model import BaseModel

class Colony(BaseModel):
    user_id = ForeignKeyField(Users, to_field="discord_id")
    species_id = ForeignKeyField(Species, to_field="id")
    server_id = CharField()
    colony_name = CharField()
