from flask.views import MethodView

class functions(MethodView):
    def get(self):
        return "Olá, Mundo!"