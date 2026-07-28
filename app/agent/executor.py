from app.core.tool_registry import registry


class Executor:
    """
    Executes the tool selected by Planner.
    """

    def execute(self, plan: dict):

        if not plan["status"]:
            print(plan["message"])
            return

        tool_name = plan["tool"]

        registry.execute(tool_name)