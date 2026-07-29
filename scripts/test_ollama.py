from app.ai.ai_engine import AIEngine

ai = AIEngine()

while True:

    cmd = input("You : ")

    if cmd.lower() == "exit":
        break

    intent = ai.get_intent(cmd)

    print("Jarvis :", intent)
    print()