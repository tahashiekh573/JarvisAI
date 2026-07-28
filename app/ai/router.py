from app.core.tool_registry import ToolRegistry


class Router:

    def __init__(self):
        self.registry = ToolRegistry()

    def execute(self, plan):

        intent = plan["intent"]

        if intent == "unknown":
            print("[ERROR] Unknown Command")
            return

        self.registry.execute(intent)