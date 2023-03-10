from abc import ABC, abstractmethod

from flask import Blueprint


class BaseRouter(ABC):
    api: Blueprint

    def __init__(self, path_router):
        self.api = Blueprint(path_router, __name__, url_prefix=path_router)
        self._register()

    @abstractmethod
    def _register(self):
        raise NotImplementedError()

    @property
    def get_router(self):
        return self.api

