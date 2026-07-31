from app.core.tool_registry import ToolRegistry


class DesktopExecutor:

    def __init__(self):
        self.registry = ToolRegistry()

    def execute(self, plan):

        steps = plan.get("steps", [])

        if not steps:
            print("[ERROR] No desktop steps.")
            return

        print("\n========== DESKTOP EXECUTION ==========\n")

        success = 0
        failed = 0

        for i, step in enumerate(steps, start=1):

            tool = step["tool"]

            print(f"[STEP {i}] {tool}")

            try:

                tool_name = tool.replace("desktop_", "")

                self.registry.execute(tool_name)

                success += 1

            except Exception as e:

                print(e)

                failed += 1

        print("\n========== SUMMARY ==========")
        print("Successful :", success)
        print("Failed :", failed)