from api_sanic.api import app
from sanic.response import json
from api_sanic.models import TodoItem


@app.route('/todo', methods=['POST'])
async def add_todo(request):
    req = request.json["todo_title"]
    user = request.json["user"]
    # todo_title = "{}".format(req)
    print(req)
    print(user)
    # TodoItem.create(todoTitle=todo_title)
    TodoItem.create(todo_title=req, user_id=user)
    return json({'message': 'added todo!'})