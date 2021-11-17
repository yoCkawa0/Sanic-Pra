import pytest
from peewee import *
# import json as pyjson
# from ..api_sanic import models
# from api_sanic import *
from api_sanic.models import *


@pytest.fixture(scope="session", autouse=True)
def create_data():
    with db.atomic() as txn:
        TodoItem.create_table()
        TodoItem.insert_many([
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

        db.execute_sql(
            "SELECT setval('todo_items_id_seq', max(id)) FROM todo_items;"
        )

        yield
        txn.rollback()
