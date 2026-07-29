from app.ai.ai_engine import AIEngine

ai = AIEngine()

while True:

    cmd = input("You : ")

    if cmd.lower() == "exit":
        break

    print()

    print("Jarvis :", ai.get_intent(cmd))

    print()