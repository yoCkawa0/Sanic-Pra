from api_sanic.api import app
from sanic.response import json
from api_sanic.models import TodoItem


@app.route('/', methods=['GET'])
async def test(request):
    return json({'hello': 'world'})


@app.route('/todos', methods=['GET'])
async def get_all_todes(request):
    todos = TodoItem.select()
    # todo = select_items()
    res = {
        "todos": []
    }
    for todo in todos:
        res["todos"].append({
            "id": todo.id,
            "todo_title": todo.todo_title
        })
    return json(res)


@app.route('/todo/<id:int>', methods=['GET'])
async def get_todo(request, id):
    todo_title = TodoItem.get(TodoItem.id == id)
    return json({id: todo_title.todo_title})
