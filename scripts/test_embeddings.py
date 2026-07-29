from app.memory.embeddings import EmbeddingModel

text = "Open Chrome Browser"

embedding = EmbeddingModel.embed(text)

print("Vector Length :", len(embedding))

print()

print("First 10 Values")

print(embedding[:10])