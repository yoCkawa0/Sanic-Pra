from api_sanic.api import app
from sanic.response import json
from api_sanic.models import Tag


@app.route('/tag', methods=['POST'])
async def add_user(request):
    tag_name = request.json["tag_name"]
    print(tag_name)
    Tag.create(tag_name=tag_name)
    return json({'message': 'added tag!'})
