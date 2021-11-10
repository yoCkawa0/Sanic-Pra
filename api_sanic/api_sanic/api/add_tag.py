from api_sanic.api import app
from sanic.response import json
from api_sanic.models import Tag


@app.route('/tag', methods=['POST'])
async def add_user(request):
    # todo_id = request.json["todo_id"]
    tag_name = request.json["tag_name"]
    # tag_id = request.json["tag_id"]
    print(tag_name)
    Tag.create(tag_name=tag_name)
    # ConnectTodo.create(todo_id=todo_id,tag_id=)
    return json({'message': 'added tag!'})
