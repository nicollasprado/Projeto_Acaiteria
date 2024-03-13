from flask.views import MethodView
from flask import request, render_template, redirect
import pymysql


class IndexController(MethodView):
    def get(self):
        return "Olá, Mundo!"
    
class LoginController(MethodView):
    def get(self):
        return render_template('public/login.html')
    
    def post(self):
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        print(first_name, last_name, email, password)
        return "produto cadastrado"