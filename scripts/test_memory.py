from app.memory.memory import Memory

memory = Memory()

memory.add("user", "Open Chrome")
memory.add("assistant", "Chrome Opened")

memory.add("user", "Open Calculator")
memory.add("assistant", "Calculator Opened")

print()

print("Conversation History")
print("--------------------")

for msg in memory.get_messages():
    print(f"{msg['role']} : {msg['content']}")

print()

print("Last Message")
print(memory.last_message())

print()

print("Total Messages :", memory.size())