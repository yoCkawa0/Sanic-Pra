from sanic import Sanic
from sanic.response import text
from sanic.response import json
from peewee import *
# import peewee as pe
# import psycopg2

from api_sanic.api import app
# from api_sanic.models import TodoItems

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
