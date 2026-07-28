from app.core.startup import startup
from app.agent.planner import Planner
from app.agent.executor import Executor


def main():

    startup()

    planner = Planner()

    executor = Executor()

    print("\n===================================")
    print("       JARVIS AI TERMINAL")
    print("===================================")
    print("Type 'exit' to quit.\n")

    while True:

        command = input("Jarvis > ")

        if command.lower() == "exit":
            print("Good Bye.")
            break

        plan = planner.plan(command)

        executor.execute(plan)


if __name__ == "__main__":
    main()