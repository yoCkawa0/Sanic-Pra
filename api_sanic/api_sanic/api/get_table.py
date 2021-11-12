from api_sanic.api import app
from sanic.response import json
from api_sanic.models import TodoItem, User, ConnectTodo, Tag
# from pprint import pprint
# from peewee import JOIN


@app.route('/todos', methods=['GET'])
async def get_all_todes(request):
    query = (
        TodoItem.select(TodoItem.id, TodoItem.todo_title, User.id, User.user_name, Tag.id, Tag.tag_name)
        .join(User)
        .switch(TodoItem)
        .join(ConnectTodo)
        .join(Tag)
    )

    res = {
        "todos": []
    }

    for q in query:
        res["todos"].append({
            "id": q.id,
            "todo_title": q.todo_title,
            "user": {
                "id": q.user.id,
                "name": q.user.user_name
            },
            "tag": {
                "id": q.connecttodo.tag_id,
                "name": q.connecttodo.tag.tag_name
            }
        })

    return json(res)


@app.route('/todo/<id:int>', methods=['GET'])
async def get_todo(request, id):
    query = (
        TodoItem.select(TodoItem.id, TodoItem.todo_title, User.id, User.user_name, Tag.id, Tag.tag_name)
        .join(User)
        .switch(TodoItem)
        .join(ConnectTodo)
        .join(Tag)
        .where(TodoItem.id == id)
    )

    res = {
        "todo": []
    }

    for q in query:
        res["todo"].append({
            "id": q.id,
            "todo_title": q.todo_title,
            "user": {
                "id": q.user.id,
                "name": q.user.user_name
            },
            "tag": {
                "id": q.connecttodo.tag_id,
                "name": q.connecttodo.tag.tag_name
            }
        })

    return json(res)
