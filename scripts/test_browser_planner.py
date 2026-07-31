from app.ai.browser_planner import BrowserPlanner

planner = BrowserPlanner()

while True:

    cmd = input("You : ")

    if cmd.lower() == "exit":
        break

    plan = planner.create_plan(cmd)

    print("\nExecution Plan")

    print(plan)

    print()