from api_sanic.api import app
from sanic.response import json
from api_sanic.models import TodoItems


@app.route('/todo', methods=['POST'])
async def add_todo(request):
    req = request.json["todoTitle"]
    todoTitle = "{}".format(req)
    print(req)
    TodoItems.create(todoTitle=todoTitle)
    return json({'!added': 'todo!'})
