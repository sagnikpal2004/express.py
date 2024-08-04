from typing import Callable

from .request import Request
from .response import Response

class Router:
    def __init__(self):
        self.routes: dict[str, Router] = {}

    def get(self, path: str, callback: Callable[[Request], Response]):
        pass

    def post(self, path: str, callback: Callable[[Request], Response]):
        pass

    def put(self, path: str, callback: Callable[[Request], Response]):
        pass

    def delete(self, path: str, callback: Callable[[Request], Response]):
        pass

    def use(self, path: str, router):
        pass