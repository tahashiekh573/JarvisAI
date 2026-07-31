from app.ai.master_agent import MasterAgent

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


agent = MasterAgent()

while True:

    cmd = input("\nYou : ")

    if cmd.lower() == "exit":
        break

    agent.execute(cmd)
    