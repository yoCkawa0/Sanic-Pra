import datetime
from peewee import *
# import peewee as pe


db = PostgresqlDatabase('postgres', host='db', port=5432, user='postgres', password='example')


class BaseModel(Model):
    class Meta:
        database = db


class TodoItem(BaseModel):
    # todoid = AutoField()
    todoTitle = CharField()
    created_time = DateTimeField(default=datetime.datetime.now)
    deleted_time = DateTimeField(default=datetime.datetime.now)

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
# db.create_tables([TodoItem, Tag, ConnectTodo])
db.create_tables([TodoItem])
db.create_tables([Tag])
db.create_tables([ConnectTodo])
