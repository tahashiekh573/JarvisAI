import ollama


class EmbeddingModel:

    MODEL_NAME = "nomic-embed-text"

    @classmethod
    def embed(cls, text: str):

        response = ollama.embeddings(
            model=cls.MODEL_NAME,
            prompt=text
        )

        return response["embedding"]