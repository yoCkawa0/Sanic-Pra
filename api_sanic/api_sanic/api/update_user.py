from api_sanic.api import app
from sanic.response import json
from api_sanic.models import User
import datetime

# update user
@app.route('/user/<id:int>', methods=['PATCH'])
async def update_tag(request, id):
    new_user_name = request.json["tag_name"]
    user = User.get(User.id == id)
    time_now = datetime.datetime.now()
    user.user_name = new_user_name
    user.update_at = time_now
    user.save()
    # user.delete_instance()
    return json({'message': 'update user!'})
