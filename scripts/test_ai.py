from app.ai.command_parser import CommandParser
from app.desktop.applications import (
    open_notepad,
    open_calculator,
    open_chrome,
    open_vscode
)
from app.core.tool_registry import ToolRegistry


registry = ToolRegistry()

registry.register("open_notepad", open_notepad)
registry.register("open_calculator", open_calculator)
registry.register("open_chrome", open_chrome)
registry.register("open_vscode", open_vscode)

parser = CommandParser()

while True:

    cmd = input("Jarvis > ")

    if cmd.lower() == "exit":
        break

    parser.execute(cmd)