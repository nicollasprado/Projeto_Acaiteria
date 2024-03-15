from src.controllers.functions import *

routes = {
    "index_route": "/home", "index_controller": IndexController.as_view("test"),
    "login_route": "/", "login_controller": LoginController.as_view("login"),
    "deleteUser_route": "/delete/user/<int:id>", "deleteUser_controller": DeleteUserController.as_view("delete_user"),
    "updateUser_route": "/update/user/<int:id>", "updateUser_controller": UpdateUserController.as_view("update_user")
} 