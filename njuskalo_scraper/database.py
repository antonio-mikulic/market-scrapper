from peewee import DateTimeField, SqliteDatabase, Model, CharField, IntegerField
from datetime import datetime
database = SqliteDatabase('njuskalo_ads.db')


def init_database():
    database.create_tables([NjuskaloAdDB])


class NjuskaloAdDB(Model):
    title = CharField()
    link = CharField(unique=True)
    description = CharField()
    published = DateTimeField()
    price = IntegerField()
    currency = CharField()
    scrappedDate = DateTimeField(default=datetime.now())

    class Meta:
        database = database
