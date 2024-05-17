import os

from peewee import SqliteDatabase, Model, CharField, IntegerField, fn, ForeignKeyField, AutoField, BooleanField

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the database path
db_path = os.path.join(BASE_DIR, 'Model', 'db.sqlite3')
db = SqliteDatabase(db_path)

# Step 3: Define your models
class BaseModel(Model):
    class Meta:
        database = db

class Chat(BaseModel):
    id = AutoField(primary_key=True)
    chat_name = CharField(max_length=64)
    chat_id = CharField(max_length=64)
    topic_id = CharField(max_length=64, null=True)
    is_forum = BooleanField()
    is_private_chat = BooleanField()



class Region(BaseModel):
    id = AutoField(primary_key=True)
    code = CharField(max_length=64, null=True)
    chat_id = ForeignKeyField(Chat, backref='regions', field='chat_id', null=True)

class Tweeter(BaseModel):
    id = AutoField(primary_key=True)
    tweeter_name = CharField(max_length=64)
    code = ForeignKeyField(Region, backref='tweeters', field='code', null=True)


if __name__ == '__main__':
    db.connect()
    db.create_tables([Chat])
    db.create_tables([Tweeter])
    db.create_tables([Region])
    db.close()


