from api_sanic.api import app
from sanic.response import json
# from api_sanic.models import TodoItem
from api_sanic.models import *


@app.route('/todo', methods=['POST'])
async def add_todo(request):
    req = request.json["todo_title"]
    todo_title = "{}".format(req)
    createdTime = datetime.datetime.now()
    print(req)
    TodoItem.create(todo_title=todo_title, createdTime=createdTime)
    return json({'!added': 'todo!'})
