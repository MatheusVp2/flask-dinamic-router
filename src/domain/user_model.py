from uuid import uuid4

from interface.i_json_serializer import JsonSerializer


class User(JsonSerializer):
    _id: str
    nome: str
    idade: int

    def __init__(self, _id=None, nome=None, idade=None):
        self._id = _id or uuid4().hex
        self.nome = nome
        self.idade = idade
