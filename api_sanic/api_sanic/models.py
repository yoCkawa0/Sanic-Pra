from peewee import *
import peewee as pe


# psql_db = PostgresqlDatabase(
#     'postgres', host='localhost', port=5555, user='postgres', password='')

psql_db = PostgresqlDatabase(
    'postgres', host='db', port=5432, user='postgres', password='example')

class TodoItems(pe.Model):
    todoTitle = pe.CharField()

    class Meta:
        database = psql_db
        table_name = 'todo_items'


psql_db.connect()
psql_db.create_tables([TodoItems])

