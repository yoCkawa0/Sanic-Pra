from sanic import Sanic
app = Sanic(__name__)

from api.add_todo import *
from api.get_todo import *
from api.delete_todo import *
from api.add_user import *
