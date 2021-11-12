from peewee import DoesNotExist
from api_sanic.api import app
from sanic.response import json
from api_sanic.models import Tag
import datetime
# from sanic.handlers import ErrorHandler
# from sanic import exceptions
from sanic.exceptions import SanicException


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
    try:
        tag = Tag.get(Tag.id == id)
        # print("========")
        # print(tag)
    except DoesNotExist:
        # raise self.model.DoesNotExist("error.", status_code=500)
        # raise Exception("error.", status_code=500)
        # raise HTTPError(404)
        raise SanicException("error.", status_code=500)
        # return json({'error_message': '存在しないIDのです.'})
        # print("error")

    res = {'message': 'update tag!'}
    time_now = datetime.datetime.now()
    tag.tag_name = new_tag_name
    tag.update_at = time_now
    tag.save()
    return json({'message': 'update tag!'})
    return json(res)


# delete tag
@ app.route('/tag/<id:int>', methods=['DELETE'])
async def delete_todo(request, id):
    tag = Tag.get(Tag.id == id)
    time_now = datetime.datetime.now()
    tag.deleted_at = time_now
    tag.save()
    # tag.delete_instance()
    return json({'message': 'deleted tag!'})


# @app.error_handler(500)
# def internal_server_error(error):
#     return json({'message': 'This id\'s todo does not exist'})
