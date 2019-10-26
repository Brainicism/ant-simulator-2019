from peewee import *
db = SqliteDatabase('main.db')

class BaseModel(Model):
    class Meta:
        database = db