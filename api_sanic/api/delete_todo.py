from api_sanic.api import app
from sanic.response import json
# from api_sanic.models import TodoItem
from api_sanic.models import *
from api_sanic.api_sanic.models import Model


@app.route('/todo/<id:int>', methods=['DELETE'])
async def delete_todo(request, id):
    todo = TodoItem.get(TodoItem.id == id)
    todo.delete_instance()
    return json({'!deleted': 'todo!'})
