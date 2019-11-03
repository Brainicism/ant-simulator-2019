import configparser
import names
from peewee import *
from models.ants import Ants
from models.colony import Colony
from models.users import Users
from models.species import Species
from models.forage_events import ForageEvents
from constants import AntRole, LifeStage

db = SqliteDatabase('main.db')
db.connect()
db.create_tables([Ants, Colony, Species, ForageEvents, Users])
config = configparser.ConfigParser()
config.read("config.ini")

if not "seed" in config:
    raise Exception("Missing seed data in config")
discord_id = config["seed"]["UserId"]
server_id = config["seed"]["ServerId"]

user_id = Users.replace(discord_id=discord_id, server_id=server_id).execute()
colony_id = Colony.insert(
    user=user_id,
    species_id=0,
    colony_name=f"Epic Colony {discord_id}",
    current_food_supply=100,
    max_food_supply=100
).execute()
test_ants = [{"colony_id": colony_id, "name": names.get_full_name(), "role": AntRole.WORKER, "life_stage": LifeStage.ADULT} for x in range(0, 10)]
Ants.insert_many(test_ants).execute()