from models.ants import Ants
from models.colony import Colony
import datetime
from peewee import fn
from collections import defaultdict
import threading
import asyncio

def trigger(client):
    current_time = datetime.datetime.now()
    asyncio.run_coroutine_threadsafe(hatch_egg_check(client, current_time), client.loop)

async def hatch_egg_check(client, current_time):
    hatched_eggs = Ants.select().where((Ants.life_stage == 0) & (Ants.birth_date < current_time - datetime.timedelta(days=3)))
    colony_egg_count = defaultdict(list)
    for egg in hatched_eggs:
        colony_egg_count[(egg.colony.user.discord_id), (egg.colony.user.server_id)] += [egg]
        egg.life_stage = 1
        egg.save()
    for colony_tuple in colony_egg_count:
        user = client.get_user(int(colony_tuple[0]))
        server = client.get_guild(int(colony_tuple[1]))
        eggs = colony_egg_count[colony_tuple]
        formatted_ant_names = [f":ant: `{egg.name}`" for egg in eggs]
        await user.send(f"Congratulations! {len(eggs)} eggs have hatched in '{server.name}'!\nPlease welcome {', '.join(formatted_ant_names)} to the family!")