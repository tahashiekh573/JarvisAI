import chromadb
from app.memory.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="./data/chroma")

        self.collection = self.client.get_or_create_collection(
            name="jarvis_memory"
        )

    def add(self, text):

        embedding = EmbeddingModel.embed(text)

        doc_id = str(self.collection.count() + 1)

        self.collection.add(
            ids=[doc_id],
            documents=[text],
            embeddings=[embedding]
        )

        print(f"[MEMORY] Stored : {text}")

    def search(self, query, top_k=3):

        embedding = EmbeddingModel.embed(query)

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

        return results["documents"][0]

    def count(self):

        return self.collection.count()

    def clear(self):

        ids = self.collection.get()["ids"]

        if ids:
            self.collection.delete(ids=ids)

        print("[MEMORY] Cleared")