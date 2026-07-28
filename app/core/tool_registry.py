from typing import Callable, Dict


class ToolRegistry:
    """
    Central registry for all executable tools.
    """

    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register(self, name: str, function: Callable):
        """
        Register a tool.
        """

        if name in self._tools:
            raise ValueError(f"Tool '{name}' is already registered.")

        self._tools[name] = function

        print(f"[REGISTERED] {name}")

    def execute(self, name: str, *args, **kwargs):
        """
        Execute a registered tool.
        """

        if name not in self._tools:
            raise ValueError(f"Tool '{name}' not found.")

        return self._tools[name](*args, **kwargs)

    def list_tools(self):
        """
        Return all registered tools.
        """

        return list(self._tools.keys())


registry = ToolRegistry()