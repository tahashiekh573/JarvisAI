from app.core.tool_registry import ToolRegistry


class Executor:

    def __init__(self):
        self.registry = ToolRegistry()

    def execute(self, plan):

        steps = plan.get("steps", [])

        if not steps:
            print("[ERROR] No steps to execute.")
            return

        print("\n========== EXECUTION ==========\n")

        for i, step in enumerate(steps, start=1):

            print(f"[STEP {i}] {step}")

            try:

                self.registry.execute(step)

                print("[SUCCESS]\n")

            except Exception as e:

                print(f"[FAILED] {e}\n")

        print("========== FINISHED ==========\n")