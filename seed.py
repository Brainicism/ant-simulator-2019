from peewee import *
from models.ants import Ants
from models.colony import Colony
from models.users import Users
from models.species import Species
from models.forage_events import ForageEvents
db = SqliteDatabase('main.db')
db.connect()
db.create_tables([Ants, Colony, Species, ForageEvents, Users])

Species.insert({
    "species_name": "Species A",
    "hp_multiplier": 1.25,
    "image_url": "https://i.imgur.com/8ICuNkT.png",
    "strength_multiplier": 1.0,
    "forage_multiplier": 0.75
}).execute()

Species.insert({
    "species_name": "Species B",
    "hp_multiplier": 0.75,
    "image_url": "https://i.imgur.com/eQw9QBk.png",
    "strength_multiplier": 1.25,
    "forage_multiplier": 1.0
}).execute()

Species.insert({
    "species_name": "Species C",
    "hp_multiplier": 1.1,
    "image_url": "https://i.imgur.com/fzb9xvm.png",
    "strength_multiplier": 1.1,
    "forage_multiplier": 1.1
}).execute()

