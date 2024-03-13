from flask import Flask
from src.routes.routes import *

app = Flask(__name__)

app.add_url_rule(routes["index_route"], view_func = routes["index_controller"])
app.add_url_rule(routes["login_route"], view_func = routes["login_controller"])

@app.errorhandler(404)
def not_found(error):
    return f"Página inexistente {error}"