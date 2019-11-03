from models.ants import Ants
from models.colony import Colony
import datetime
from peewee import fn
from collections import defaultdict

def trigger():
    current_time = datetime.datetime.now()
    hatch_egg_check(current_time)


def hatch_egg_check(current_time):
    hatched_eggs = Ants.select().where((Ants.life_stage == 0) & (Ants.birth_date < current_time - datetime.timedelta(days=3)))
    colony_egg_count = defaultdict(int)
    for egg in hatched_eggs:
        colony_egg_count[egg.colony_id] += 1
        egg.life_stage = 1
        egg.save()
    for colony_id in colony_egg_count:
        print(f"Colony {colony_id} has hatched {colony_egg_count[colony_id]} eggs")