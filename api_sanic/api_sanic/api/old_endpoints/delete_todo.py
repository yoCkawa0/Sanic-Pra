from api_sanic.api import app
from sanic.response import json
from api_sanic.models import TodoItem
import datetime


@app.route('/todo/<id:int>', methods=['DELETE'])
async def delete_todo(request, id):
    todo = TodoItem.get(TodoItem.id == id)
    time_now = datetime.datetime.now()
    todo.deleted_at = time_now
    todo.save()
    # todo.delete_instance()
    return json({'message': 'deleted todo!'})
