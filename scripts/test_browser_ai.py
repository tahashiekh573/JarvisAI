from app.ai.browser_planner import BrowserPlanner
from app.ai.browser_executor import BrowserExecutor

planner = BrowserPlanner()
executor = BrowserExecutor()

while True:

    cmd = input("You : ")

    if cmd.lower() == "exit":
        break

    plan = planner.create_plan(cmd)

    print("\nExecution Plan")

    print(plan)

    executor.execute(plan)