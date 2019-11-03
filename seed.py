from peewee import *
from models.ants import Ants
from models.colony import Colony
from models.users import Users
from models.species import Species
from models.forage_events import ForageEvents
from models.shop_items import ShopItems
import json


def seed():
    print("Seeding database...")
    db = SqliteDatabase('main.db')
    db.connect()
    db.create_tables([Ants, Colony, Species, ForageEvents, ShopItems, Users])

    for species in parse_json_from_file("data/species.json"):
        Species.replace({
            "id": species["id"],
            "species_name": species["species_name"],
            "hp_multiplier": species["hp_multiplier"],
            "image_url": species["image_url"],
            "strength_multiplier": species["strength_multiplier"],
            "forage_multiplier": species["forage_multiplier"]
        }).execute()

    for event in parse_json_from_file("data/forage_events.json"):
        ForageEvents.replace({
            "id": event["id"],
            "event_description": event["description"],
            "event_rarity": event["rarity"],
            "event_death_multiplier": event["death_multiplier"],
            "event_food_multiplier": event["food_multiplier"],
            "image_url": event["image_url"]
        }).execute()

    for shop_item in parse_json_from_file("data/shop_items.json"):
        ShopItems.replace({
            "id": shop_item["id"],
            "name": shop_item["name"],
            "description": shop_item["description"],
            "price": shop_item["price"]
        }).execute()

    db.close()


if __name__ == '__main__':
    seed()


def parse_json_from_file(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data
