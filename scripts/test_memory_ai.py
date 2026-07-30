from app.ai.ai_engine import AIEngine

ai = AIEngine()

while True:

    cmd = input("You : ")

    if cmd == "exit":
        break

    intent = ai.get_intent(cmd)

    print("Intent :", intent)