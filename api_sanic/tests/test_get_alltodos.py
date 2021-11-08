from api_sanic.api import app


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
