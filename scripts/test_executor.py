from app.ai.reasoning import ReasoningEngine
from app.ai.executor import Executor

from app.desktop.applications import (
    open_chrome,
    open_calculator,
    open_notepad,
    open_vscode
)

from app.core.tool_registry import ToolRegistry

registry = ToolRegistry()

registry.register("open_chrome", open_chrome)
registry.register("open_calculator", open_calculator)
registry.register("open_notepad", open_notepad)
registry.register("open_vscode", open_vscode)

reasoner = ReasoningEngine()
executor = Executor()

while True:

    cmd = input("You : ")

    if cmd.lower() == "exit":
        break

    plan = reasoner.create_plan(cmd)

    print("\nExecution Plan")
    print(plan)

    executor.execute(plan)