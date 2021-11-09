from api_sanic.api import app
from sanic.response import json
from api_sanic.models import User
import datetime


@app.route('/user/<id:int>', methods=['DELETE'])
async def delete_todo(request, id):
    user = User.get(User.id == id)
    time_now = datetime.datetime.now()
    user.deleted_at = time_now
    user.save()
    # todo.delete_instance()
    return json({'message': 'deleted user!'})
