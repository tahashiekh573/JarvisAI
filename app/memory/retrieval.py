from app.memory.vector_store import VectorStore


class Retrieval:

    def __init__(self):
        self.store = VectorStore()

    def remember(self, text):
        self.store.add(text)

    def recall(self, query, top_k=3):
        return self.store.search(query, top_k)

    def clear(self):
        self.store.clear()