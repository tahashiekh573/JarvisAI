from ollama import chat
from app.memory.retrieval import Retrieval
from app.memory.conversation_memory import ConversationMemory


class AIEngine:

    def __init__(self):

        self.retrieval = Retrieval()
        self.conversation = ConversationMemory()

    def get_intent(self, command):

        # -----------------------------
        # Long-Term Memory
        # -----------------------------
        memories = self.retrieval.recall(command)

        if memories:
            long_memory = "\n".join(f"- {m}" for m in memories)
        else:
            long_memory = "No previous memories."

        # -----------------------------
        # Short-Term Memory
        # -----------------------------
        short_memory = self.conversation.format_history()

        # -----------------------------
        # Prompt
        # -----------------------------
        prompt = f"""
You are an intent classifier.

Conversation History:
{short_memory}

Relevant Memories:
{long_memory}

User Command:
{command}

Available Intents:

open_chrome
open_calculator
open_vscode
open_notepad
unknown

Rules:
- Return ONLY one intent from the list above.
- Do NOT explain.
- Do NOT write sentences.
- Do NOT write markdown.
- Output must exactly match one item.

Intent:
"""

        response = chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # -----------------------------
        # Raw LLM Output
        # -----------------------------
        raw_output = response["message"]["content"].strip().lower()

        print(f"[LLM] {raw_output}")

        # -----------------------------
        # Clean Intent
        # -----------------------------
        valid_intents = [
            "open_chrome",
            "open_calculator",
            "open_vscode",
            "open_notepad",
            "unknown"
        ]

        intent = "unknown"

        for item in valid_intents:
            if item in raw_output:
                intent = item
                break

        # -----------------------------
        # Save Short-Term Memory
        # -----------------------------
        self.conversation.add("User", command)
        self.conversation.add("Assistant", intent)

        # -----------------------------
        # Save Long-Term Memory
        # -----------------------------
        self.retrieval.remember(f"User: {command}")
        self.retrieval.remember(f"Intent: {intent}")

        return intent