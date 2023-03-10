from os import walk
import platform

from enumerator import SystemEnum


class RouterModulePaths:

    def __lambda_filter_paths_router(self, dados):
        rel_path, paths, files = dados
        if "__pycache__" not in rel_path and "__init__.py" in files:
            return rel_path

    def __get_paths_router(self, relative_path):
        paths_in_routes = walk(relative_path)
        return list(filter( self.__lambda_filter_paths_router, paths_in_routes ))

    def __get_prefix_router_modules(self, paths_router, relative_path, router_path):
        only_paths = [ item[0].replace(relative_path, "") for item in paths_router ]
        platform_system = platform.system()
        router_modules = []
        for item in only_paths:
            prefix, module = "", ""
            if platform_system.lower() == SystemEnum.WINDOWS.value.lower():
                prefix = item.replace("\\", "/")
                module = f"{router_path}{prefix}".replace("/", ".")
            if platform_system.lower() == SystemEnum.LINUX.value.lower():
                prefix = item.replace("/", "")
                module = f"{router_path}{prefix}".replace("/", ".")
            router_modules.append({
                "prefix" : prefix,
                "module" : module
            })
        return router_modules

    def get(self, relative_path, router_path):
        paths_router = self.__get_paths_router(relative_path)
        return self.__get_prefix_router_modules(paths_router, relative_path, router_path)