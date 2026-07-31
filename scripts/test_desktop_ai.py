from app.ai.desktop_planner import DesktopPlanner
from app.ai.desktop_executor import DesktopExecutor

from app.desktop.applications import (
    open_chrome,
    open_calculator,
    open_notepad,
    open_vscode,
)

from app.core.tool_registry import ToolRegistry


registry = ToolRegistry()

registry.register("open_chrome", open_chrome)
registry.register("open_calculator", open_calculator)
registry.register("open_notepad", open_notepad)
registry.register("open_vscode", open_vscode)


planner = DesktopPlanner()
executor = DesktopExecutor()

while True:

    cmd = input("You : ")

    if cmd.lower() == "exit":
        break

    plan = planner.create_plan(cmd)

    print("\nExecution Plan")
    print(plan)

    executor.execute(plan)