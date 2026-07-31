from app.ai.tool_router import ToolRouter

router = ToolRouter()

while True:

    cmd = input("You : ")

    if cmd.lower() == "exit":
        break

    planner = router.route(cmd)

    print("Planner :", planner)