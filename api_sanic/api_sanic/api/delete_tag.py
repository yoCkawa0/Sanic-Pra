from api_sanic.api import app
from sanic.response import json
from api_sanic.models import Tag
import datetime


@app.route('/tag/<id:int>', methods=['DELETE'])
async def delete_todo(request, id):
    tag = Tag.get(Tag.id == id)
    time_now = datetime.datetime.now()
    tag.deleted_at = time_now
    tag.save()
    # todo.delete_instance()
    return json({'message': 'deleted tag!'})
