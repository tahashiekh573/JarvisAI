from app.memory.retrieval import Retrieval

memory = Retrieval()

memory.clear()

memory.remember("I like Java")
memory.remember("I use Spring Boot")
memory.remember("My IDE is VS Code")
memory.remember("I work with Python")

print()

print("Searching...")

results = memory.recall("Which IDE do I use?")

for item in results:
    print(item)