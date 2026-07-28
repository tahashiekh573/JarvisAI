from typing import Callable, Dict

class ToolRegistry:

    _instance = None
    _tools = {}

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def register(self, name, func):

        self._tools[name] = func

        print(f"[REGISTERED] {name}")

    def execute(self, name, *args, **kwargs):

        if name not in self._tools:
            raise ValueError(f"Tool '{name}' not found.")

        return self._tools[name](*args, **kwargs)

    def list_tools(self):

        return list(self._tools.keys())

registry = ToolRegistry()