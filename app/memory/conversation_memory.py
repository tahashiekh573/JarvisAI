from collections import deque


class ConversationMemory:

    def __init__(self, max_messages=10):
        self.history = deque(maxlen=max_messages)

    def add(self, role, content):
        self.history.append({
            "role": role,
            "content": content
        })

    def get_history(self):
        return list(self.history)

    def clear(self):
        self.history.clear()

    def format_history(self):

        if not self.history:
            return "No conversation history."

        lines = []

        for msg in self.history:
            lines.append(f"{msg['role']}: {msg['content']}")

        return "\n".join(lines)