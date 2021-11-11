from api_sanic.api import app
from sanic.response import json
from api_sanic.models import TodoItem, User, ConnectTodo, Tag
from pprint import pprint
from peewee import JOIN


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

    # query = (TodoItem.select(TodoItem, Tag)
    #          .join(ConnectTodo)
    #          .join(Tag)
    #          )

    # query = (TodoItem
    #          .select(TodoItem.id, TodoItem.todo_title, User.user_name, Tag.tag_name)
    #          .join(User)
    #          .where(User.id == TodoItem.user_id)
    #          .join(ConnectTodo, JOIN.LEFT_OUTER)
    #           .swith(TodoItem)
    #          )
    query = (TodoItem.select(TodoItem.id, TodoItem.todo_title, User.id, User.user_name, Tag.id, Tag.tag_name)
             #   .join(User)
             #  .where(User.id == TodoItem.user_id)
             #  .join(ConnectTodo)
             .join(User)
             .switch(TodoItem)
             #  .join(ConnectTodo, JOIN.LEFT_OUTER)
             .join(ConnectTodo)
             .join(Tag)
             # .swith(TodoItem)
             #  .where(User.id == TodoItem.user_id)
             )

    # for q in query:
    #     tag: Tag = q.connecttodo.tag
    #     user: User = q.user

    #     # pprint(vars(q))
    #     print("================111")
    #     # pprint(vars(tag))
    #     print("================222")
    #     # pprint(vars(user))
    #     break

    res2 = {
        "todos": []
    }

    for q in query:
        res2["todos"].append({
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

# ===================
    # res = {
    #     "todos": []
    # }
    # for todo in todos:
    #     res["todos"].append({
    #         "id": todo.id,
    #         "todo_title": todo.todo_title,
    #         "user": {
    #             "id": todo.user_id,
    #             "name": todo.user.user_name
    #         },
    #         # "tag": {
    #         #     "id": todo.tag_id,
    #         #     "name": todo.tag.tag_name
    #         # }

    #     })

# =========================
    return json(res2)


@app.route('/todo/<id:int>', methods=['GET'])
async def get_todo(request, id):
    todo_title = TodoItem.get(TodoItem.id == id)
    return json({id: todo_title.todo_title})
