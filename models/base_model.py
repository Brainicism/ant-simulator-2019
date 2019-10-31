from peewee import *
db = SqliteDatabase('main.db', pragmas={
    'foreign_keys': 1,
})

class BaseModel(Model):
    class Meta:
        database = db
        legacy_table_names = False
