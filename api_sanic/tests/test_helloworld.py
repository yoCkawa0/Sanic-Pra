from api_sanic.api import app


def test_hello(request):
    _, response = app.test_client.get('/')
    print(response.json)
    assert response.json == ({'hello': 'world'})
