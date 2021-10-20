from sanic import Sanic
from sanic.response import text
from sanic.response import json
from peewee import *
import peewee as pe
import psycopg2


psql_db = PostgresqlDatabase(
    'testdb', host='localhost', port=8881, user='postgres', password='example')


class TodoItems(pe.Model):
    todoTitle = pe.CharField()

    class Meta:
        database = psql_db
        table_name = 'todo_items'


psql_db.connect()
psql_db.create_tables([TodoItems])


app = Sanic(__name__)


@app.route('/', methods=['GET'])
async def test(request):
    return json({'hello': 'world'})


@app.route('/todos', methods=['GET'])
async def get_all_todes(request):
    todos = TodoItems.select()
    res = {
        "todos": []
    }
    for todo in todos:
        res["todos"].append({
            "id": todo.id,
            "todoTitle": todo.todoTitle
        })
    return json(res)


@app.route('/todo/<id:int>', methods=['GET'])
async def get_todo(request, id):
    todotitle = TodoItems.get(TodoItems.id == id)
    return json({id: todotitle.todoTitle})


@app.route('/todo', methods=['POST'])
async def add_todo(request):
    req = request.json["todoTitle"]
    todoTitle = "{}".format(req)
    print(req)
    TodoItems.create(todoTitle=todoTitle)
    return json({'!added': 'todo!'})


@app.route('/todo/<id:int>', methods=['DELETE'])
async def delete_todo(request, id):
    todo = TodoItems.get(TodoItems.id == id)
    todo.delete_instance()
    return json({'!deleted': 'todo!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
