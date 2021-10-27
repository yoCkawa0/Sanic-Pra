from api_sanic.api import app
from sanic.response import json
from api_sanic.models import TodoItems

@app.route('/', methods=['GET'])
async def test(request):
    return json({'hello': 'world'})


# def select_items():
#     return TodoItems.select()


# def get_all_todos(db):
#     return db.select(Todos)


@app.route('/todos', methods=['GET'])
async def get_all_todes(request):
    todos = TodoItems.select()
    # todo = select_items()
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
