import datetime
from peewee import *
# import peewee as pe


db = PostgresqlDatabase('postgres', host='db', port=5432, user='postgres', password='example')


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    deleted_at = DateTimeField(null=True)

    class Meta:
        database = db


class User(BaseModel):
    # userid = AutoField()
    user_name = CharField()

    class Meta:
        table_name = "users"


class TodoItem(BaseModel):
    # todoid = AutoField()
    todo_title = CharField()
    user = ForeignKeyField(User, backref='todo_items')
    # createdTime = TimestampField()
    # created_at = DateTimeField(default=datetime.datetime.now)
    # updated_at = DateTimeField(default=datetime.datetime.now)
    # deleted_at = DateTimeField(null=True)

    class Meta:
        table_name = "todo_items"


class Tag(BaseModel):
    # tagid = AutoField()
    tag_name = CharField()

    class Meta:
        table_name = "tags"


class ConnectTodo(BaseModel):
    # connectid = AutoField()
    todo = ForeignKeyField(TodoItem, backref='connect_todos')
    tag = ForeignKeyField(Tag, backref='connect_todos')

    class Meta:
        table_name = "connect_todos"


db.connect()
db.create_tables([User, TodoItem, Tag, ConnectTodo])
# db['users'].create_index(['username'], unique=True)

# db.create_tables([Tag])
# db.create_tables([User])
# db.create_tables([TodoItem])
# db.create_tables([ConnectTodo])
