from flask import Flask
from src.routes.routes import *

app = Flask(__name__)

app.add_url_rule(routes["functions_route"], view_func=routes["rFunctions"])