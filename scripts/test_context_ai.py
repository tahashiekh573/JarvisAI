from app.ai.ai_engine import AIEngine

ai = AIEngine()

while True:

    command = input("You : ")

    if command == "exit":
        break

    intent = ai.get_intent(command)

    print("Intent :", intent)