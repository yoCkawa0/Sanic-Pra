import pytest
from peewee import *
import json as pyjson
from ..main import *


@pytest.fixture(scope="session", autouse=True)
def create_data():
    with psql_db.atomic() as txn:
        TodoItems.create_table()
        TodoItems.insert_many([
            {"id": 1, "todoTitle": "task1"},
            {"id": 2, "todoTitle": "task2"},
            {"id": 3, "todoTitle": "task1"},
            {"id": 4, "todoTitle": "task2"},
            {"id": 5, "todoTitle": "task100"},
            {"id": 6, "todoTitle": "task100"},
            {"id": 9, "todoTitle": "task100"},
            {"id": 20, "todoTitle": "task100"},
            {"id": 10, "todoTitle": "task100"},
            {"id": 11, "todoTitle": "task100"}
        ]).execute()

        psql_db.execute_sql(
            "SELECT setval('todo_items_id_seq', max(id)) FROM todo_items;"
        )

        yield
        txn.rollback()


def test_hello(request):
    _, response = app.test_client.get('/')
    print(response.json)
    assert response.json == ({'hello': 'world'})


def test_get_todo(request):
    _, response = app.test_client.get('/todo/11')
    print(response.json)
    assert response.json == ({"11": "task100"})


def test_get_all_todos(request):
    _, response = app.test_client.get('/todos')
    print(response.json)
    assert response.json == {
        "todos": [
            {"id": 1, "todoTitle": "task1"},
            {"id": 2, "todoTitle": "task2"},
            {"id": 3, "todoTitle": "task1"},
            {"id": 4, "todoTitle": "task2"},
            {"id": 5, "todoTitle": "task100"},
            {"id": 6, "todoTitle": "task100"},
            {"id": 9, "todoTitle": "task100"},
            {"id": 20, "todoTitle": "task100"},
            {"id": 10, "todoTitle": "task100"},
            {"id": 11, "todoTitle": "task100"}
        ]
    }


def test_delete_todo(request):
    _, response = app.test_client.delete('todo/11')
    checktodo = TodoItems.get_or_none(TodoItems.id == 11)
    assert checktodo == None


def test_add_todo(request):
    with psql_db.atomic()as txn:
        assert len(TodoItems.select().where(
            TodoItems.todoTitle == "task200"
        )) == 0
        data = {"todoTitle": "task200"}
        _, response = app.test_client.post(
            'todo', data=pyjson.dumps(data)
        )
        assert response.json == {'!added': 'todo!'}
        assert len(TodoItems.select().where(
            TodoItems.todoTitle == "task200"
        )) == 1
        txn.rollback()
