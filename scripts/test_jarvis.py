from app.ai.ai_engine import AIEngine
from app.core.tool_registry import ToolRegistry

from app.desktop.applications import (
    open_calculator,
    open_chrome,
    open_notepad,
    open_vscode,
)

ai = AIEngine()

registry = ToolRegistry()

registry.register("open_calculator", open_calculator)
registry.register("open_chrome", open_chrome)
registry.register("open_notepad", open_notepad)
registry.register("open_vscode", open_vscode)

print("=" * 50)
print("JARVIS AI")
print("=" * 50)

while True:

    command = input("\nYou : ")

    if command.lower() == "exit":
        break

    intent = ai.get_intent(command)

    print("AI :", intent)

    try:
        registry.execute(intent)
    except Exception:
        print("[INFO] I don't know how to perform this task.")