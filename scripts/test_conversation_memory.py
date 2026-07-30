from app.memory.conversation_memory import ConversationMemory

memory = ConversationMemory()

memory.add("User", "Open Chrome")
memory.add("Assistant", "Chrome Opened")

memory.add("User", "Open Calculator")
memory.add("Assistant", "Calculator Opened")

print(memory.format_history())