from src.controllers.functions import *

routes = {
    "index_route": "/home", "index_controller": IndexController.as_view("Test"),
    "login_route": "/", "login_controller": LoginController.as_view("Login")
} 