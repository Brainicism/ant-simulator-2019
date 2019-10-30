from peewee import *
from models.ants import Ants
from models.colony import Colony
from models.users import Users
from models.species import Species
from models.forage_events import ForageEvents
db = SqliteDatabase('main.db')
db.connect()
db.create_tables([Ants, Colony, Species, ForageEvents, Users])

for discord_id in range(0, 5):
    user_id = Users.insert(discord_id=discord_id, server_id=100).execute()
    colony_id = Colony.insert(
        user_id=user_id,
        species_id=0,
        colony_name=f"Epic Colony {discord_id}"
    ).execute()

    test_ants = [{"colony_id": colony_id, "name": f"ant-{str(x)}", "role": 'worker', "life_stage": 3 } for x in range(0,10)]
    Ants.insert_many(test_ants).execute()