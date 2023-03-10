from flask import jsonify

from domain.user_model import User
from interface.i_base_router import BaseRouter


class UserRouter(BaseRouter):

    def __init__(self, prefixo):
        self.path = "/endecero"
        self.path_router = prefixo + self.path
        super().__init__(self.path_router)

    def _register(self):
        @self.api.route("/")
        def get_usuario():
            novo = User(nome="Matheus", idade=24).from_json()
            return jsonify(novo), 200
