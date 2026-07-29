from app.ai.ai_engine import AIEngine
from app.ai.command_parser import CommandParser
from app.desktop.applications import (
    open_notepad,
    open_calculator,
    open_chrome,
    open_vscode
)
from app.core.tool_registry import ToolRegistry

# Tool Registry
registry = ToolRegistry()

registry.register("open_notepad", open_notepad)
registry.register("open_calculator", open_calculator)
registry.register("open_chrome", open_chrome)
registry.register("open_vscode", open_vscode)

# AI + Parser
ai = AIEngine()
parser = CommandParser()

while True:

    cmd = input("You : ")

    if cmd.lower() == "exit":
        break

    # AI Intent
    intent = ai.get_intent(cmd)

    print("[AI]", intent)

    # Execute Tool
    parser.execute(intent)