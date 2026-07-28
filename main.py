from app.core.startup import startup
from app.core.tool_registry import registry


def main():
    startup()

    print("\nAvailable Tools\n")

    for tool in registry.list_tools():
        print("-", tool)

    print("\nTesting Chrome...\n")

    # registry.execute("open_chrome")

    # Test VS Code
    # registry.execute("open_vscode")

    # Test Calculator
    registry.execute("open_calculator")


if __name__ == "__main__":
    main()