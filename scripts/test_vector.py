from app.memory.vector_store import VectorStore

db = VectorStore()

db.clear()

db.add("Open Chrome Browser")

db.add("Open Calculator")

db.add("Launch VS Code")

db.add("Search Google")

print()

print("Total Documents :", db.count())

print()

print("Searching...")

results = db.search("open browser")

for r in results:
    print(r)