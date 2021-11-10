from api_sanic.api import app
from sanic.response import json
from api_sanic.models import TodoItem
import datetime


@app.route('/todo/<id:int>', methods=['PATCH'])
async def update_todo(request, id):
    new_todo_title = request.json["todo_title"]
    new_user = request.json["user"]
    todo = TodoItem.get(TodoItem.id == id)
    time_now = datetime.datetime.now()
    todo.todo_title = new_todo_title
    todo.user = new_user
    todo.update_at = time_now
    todo.save()
    # todo.delete_instance()
    return json({'message': 'update todo!'})
