from src.app import app

HOST = 'localhost'
POST = 5000
DEBUG = True

if (__name__ == '__main__'):
    app.run(HOST, POST, DEBUG)