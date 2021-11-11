from api_sanic.api import app
from sanic.response import json
from api_sanic.models import User


@app.route('/user', methods=['POST'])
async def add_user(request):
    user_name = request.json["user_name"]
    # user = "{}".format(user)
    print(user_name)
    # TodoItem.create(todoTitle=todo_title)
    User.create(user_name=user_name)
    return json({'message': 'added user!'})
