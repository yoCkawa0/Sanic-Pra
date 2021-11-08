from api_sanic.api import app


def test_get_todo(request):
    _, response = app.test_client.get('/todo/11')
    print(response.json)
    assert response.json == ({"11": "task100"})
