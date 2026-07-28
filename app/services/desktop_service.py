from app.core.tool_registry import registry
from app.desktop.applications import (
    open_notepad,
    open_calculator,
    open_chrome,
    open_vscode,
)


def register_desktop_tools():

    registry.register("open_notepad", open_notepad)
    registry.register("open_calculator", open_calculator)
    registry.register("open_chrome", open_chrome)
    registry.register("open_vscode", open_vscode)