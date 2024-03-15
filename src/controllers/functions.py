from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import mysql


cursor = mysql.cursor()


class IndexController(MethodView):
    def get(self):
        return "Olá, Mundo!"
    
class LoginController(MethodView):
    def get(self):
        cursor.execute("SELECT * FROM users")
        dataDB = cursor.fetchall()
        return render_template('public/login.html', data = dataDB)
    
    def post(self):
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, password))
        cursor.connection.commit()
        return redirect('/')
        
class DeleteUserController(MethodView):
    def post(self, id):
        cursor.execute("DELETE FROM users WHERE id = %s", (id))
        cursor.connection.commit()
        return redirect('/')
    
class UpdateUserController(MethodView):
    def get(self, id):
        cursor.execute("SELECT * FROM users WHERE id = %s", (id))
        user = cursor.fetchone()
        return render_template('public/update.html', users = user)
    
    def post(self, id):
        newFirstName = request.form['new_first_name']
        newLastName = request.form['new_last_name']
        newEmail = request.form['new_email']
        newPassword = request.form['new_password']

        if (newFirstName == ''):
            newFirstName = cursor.execute("SELECT first_name FROM users WHERE id = %s", (id))
            newFirstName = cursor.fetchone()
        if (newLastName == ''):
            newLastName = cursor.execute("SELECT last_name FROM users WHERE id = %s", (id))
            newLastName = cursor.fetchone()
        if (newEmail == ''):
            newEmail = cursor.execute("SELECT email FROM users WHERE id = %s", (id))
            newEmail = cursor.fetchone()
        if (newPassword == ''):
            newPassword = cursor.execute("SELECT password FROM users WHERE id = %s", (id))
            newPassword = cursor.fetchone()

        cursor.execute("UPDATE users SET first_name = %s, last_name = %s, email = %s, password = %s WHERE id = %s", (newFirstName, newLastName, newEmail, newPassword, id))
        cursor.connection.commit()
        return redirect('/')