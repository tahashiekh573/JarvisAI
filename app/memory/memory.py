class Memory:

    def __init__(self, max_messages=20):
        self.max_messages = max_messages
        self.messages = []

    def add(self, role, content):
        """
        role: user / assistant / system
        content: message text
        """

        self.messages.append({
            "role": role,
            "content": content
        })

        # Sirf last N messages memory me rakho
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def get_messages(self):
        return self.messages

    def clear(self):
        self.messages.clear()

    def last_message(self):

        if not self.messages:
            return None

        return self.messages[-1]

    def size(self):
        return len(self.messages)