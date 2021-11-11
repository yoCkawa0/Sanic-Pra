from api_sanic.api import app
from sanic.response import json


@app.route('/', methods=['GET'])
async def test(request):
    return json({'hello': 'world'})
