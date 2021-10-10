from sanic.response import text
from sanic.response import json
from sanic import Sanic

todoitems = [
    {"id": 1, "title": "aaa"},
    {"id": 2, "title": "bbb"},
    {"id": 3, "title": "homeworks"},
    {"id": 4, "title": "flask"},
    {"id": 5, "title": "sanic"}
]


app = Sanic(__name__)


@app.route('/', methods=['GET'])
async def test(request):
    return json({'hello': 'world'})


@app.route('/posts', methods=['GET'])
async def get_allitems(request):
    return json(todoitems)


@app.route('/posts/<id:int>', methods=['GET'])
async def get_item(request, id):
    return json(todoitems[id-1])


@app.route('/posts/add', methods=['POST'])
async def add_item(request):
    item = request.json
    todoitems.append(item)
    # print(todoitems)
    return json(todoitems)


@app.route('/posts/update/<id:int>', methods=['PUT'])
async def update_item(request, id):
    item = request.json
    todoitems[id-1] = item
    return json(todoitems)


@app.route('/posts/delete/<id:int>', methods=['DELETE'])
async def delete_item(request, id):
    id -= 1
    todoitems.pop(id)
    return json(todoitems)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
