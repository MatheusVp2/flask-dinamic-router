import inspect
from os import path, getcwd, walk
from pydoc import locate

from flask import Flask

import platform

from enumerator import SystemEnum

from helper import RouterModulePaths, router_module_paths

class FlaskCreateApp:
    app: Flask
    router_path: str

    def __init__(self):
        self.__name__ = "MicroServiceFlask"
        self.router_path = "routes"
        self.app = Flask(__name__)
        self.init_routes()

    def init_routes(self):
        relative_path = path.join(getcwd(), "src", self.router_path)
        routers_modules = RouterModulePaths().get(relative_path, self.router_path)
        for router in routers_modules:
            prefix = router.get("prefix")
            module = router.get("module")
            path_import = inspect.getmembers( locate( module ) )
            for name, Router in path_import:
                if inspect.isclass(Router):
                    print(f"Registrando => Class: {name} na Rota: {prefix}")
                    self.app.register_blueprint(Router(prefix).get_router)
                    

    def start(self):
        self.app.run(host="0.0.0.0", port=5000, debug=True)
