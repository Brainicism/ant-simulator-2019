from peewee import *
from models.ants import Ants
from models.colony import Colony
from models.users import Users
from models.species import Species
from models.forage_events import ForageEvents
db = SqliteDatabase('main.db')
db.connect()
db.create_tables([Ants, Colony, Species, ForageEvents, Users])

Species.replace({
    "id": 1,
    "species_name": "Carpenter Ants",
    "hp_multiplier": 1.25,
    "image_url": "https://cdn.discordapp.com/attachments/197012817134616577/639316147891732491/JPEG_20190927_214519.jpg",
    "strength_multiplier": 1.0,
    "forage_multiplier": 0.75
}).execute()

Species.replace({
    "id": 2,
    "species_name": "Yellow Crazy Ants",
    "hp_multiplier": 0.75,
    "image_url": "https://invasives.org.au/wp-content/uploads/2016/04/fs-yellow-crazy-ant.jpg",
    "strength_multiplier": 1.25,
    "forage_multiplier": 1.0
}).execute()

Species.replace({
    "id": 3,
    "species_name": "Fire Ants",
    "hp_multiplier": 1.1,
    "image_url": "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2014/12/8/1418073100561/44f3fbab-89c8-4a1f-95b5-b330cb6d8523-1020x612.jpeg?width=620&quality=85&auto=format&fit=max&s=ae46ffd7415131288c781d7985b0c2d8",
    "strength_multiplier": 1.1,
    "forage_multiplier": 1.1
}).execute()
