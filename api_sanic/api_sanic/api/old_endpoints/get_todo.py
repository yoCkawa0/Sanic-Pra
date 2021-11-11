from api_sanic.api import app
from sanic.response import json
from api_sanic.models import TodoItem, User, ConnectTodo, Tag
from pprint import pprint


# @app.route('/', methods=['GET'])
# async def test(request):
#     return json({'hello': 'world'})


@app.route('/todos', methods=['GET'])
async def get_all_todes(request):
    todos = TodoItem.select()
    # query = TodoItem.select(TodoItem, User,Tag).join(User).switch(TodoItem).join(Tag)
    # ConnectTodo.select(ConnectTodo, TodoItem).join(TodoItem)
    # ConnectTodo.select(ConnectTodo, Tag).join(Tag)
    # query = (ConnectTodo
    #          .select(ConnectTodo, TodoItem)
    #          .join(Tag)
    #          .switch(ConnectTodo)
    #          )
    query = (TodoItem.select(TodoItem, Tag)
             .join(ConnectTodo)
             .join(Tag)
             )

    for q in query:
        tag: Tag = q.connecttodo.tag
        user: User = q.user

        pprint(vars(q))
        pprint(vars(tag))
        pprint(vars(user))
        break
        # pprint(vars(q))

    # todo = select_items()
    res = {
        "todos": []
    }
    for todo in todos:
        res["todos"].append({
            "id": todo.id,
            "todo_title": todo.todo_title,
            # "created_at": todo.created_at,
            # "updated_at": todo.updated_at,
            "user": {
                "id": todo.user_id,
                "name": todo.user.user_name
            },
            # "tag": {
            #     "id": todo.tag_id,
            #     "name": todo.tag.tag_name
            # }

        })
    return json(res)


@app.route('/todo/<id:int>', methods=['GET'])
async def get_todo(request, id):
    todo_title = TodoItem.get(TodoItem.id == id)
    return json({id: todo_title.todo_title})

"""
    todo_id
    todo_title
    user_id
    user_name
    tag_id
    tag_name
"""
