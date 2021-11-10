from api_sanic.api import app
from sanic.response import json
from api_sanic.models import Tag
import datetime

# add tag
@app.route('/tag', methods=['POST'])
async def add_tag(request):
    tag_name = request.json["tag_name"]
    print(tag_name)
    Tag.create(tag_name=tag_name)
    return json({'message': 'added tag!'})


# update tag
@app.route('/tag/<id:int>', methods=['PATCH'])
async def update_tag(request, id):
    new_tag_name = request.json["tag_name"]
    tag = Tag.get(Tag.id == id)
    time_now = datetime.datetime.now()
    tag.tag_name = new_tag_name
    tag.update_at = time_now
    tag.save()
    
    return json({'message': 'update tag!'})


# delete tag
@app.route('/tag/<id:int>', methods=['DELETE'])
async def delete_todo(request, id):
    tag = Tag.get(Tag.id == id)
    time_now = datetime.datetime.now()
    tag.deleted_at = time_now
    tag.save()
    # tag.delete_instance()
    return json({'message': 'deleted tag!'})