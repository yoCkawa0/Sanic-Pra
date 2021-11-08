from api_sanic.api import app
from api_sanic.models import *


def test_delete_todo(request):
    _, response = app.test_client.delete('todo/11')
    checktodo = TodoItem.get_or_none(TodoItem.id == 11)
    assert checktodo == None
