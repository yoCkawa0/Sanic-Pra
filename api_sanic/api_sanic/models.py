from peewee import *
import peewee as pe


psql_db = PostgresqlDatabase(
    'testdb', host='localhost', port=8881, user='postgres', password='example')

class TodoItems(pe.Model):
    todoTitle = pe.CharField()

    class Meta:
        database = psql_db
        table_name = 'todo_items'


psql_db.connect()
psql_db.create_tables([TodoItems])

