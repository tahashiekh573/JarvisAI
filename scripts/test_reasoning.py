from app.ai.reasoning import ReasoningEngine

reasoner = ReasoningEngine()

while True:

    cmd = input("You : ")

    if cmd == "exit":
        break

    plan = reasoner.create_plan(cmd)

    print()
    print("Execution Plan")
    print(plan)
    print()