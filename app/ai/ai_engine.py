from ollama import chat


class AIEngine:

    SYSTEM_PROMPT = """
You are Jarvis AI.

Convert the user's command into ONLY one of these intents:

open_chrome
open_calculator
open_vscode
open_notepad
unknown

Reply ONLY with the intent.
"""

    def get_intent(self, command: str):

        response = chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": self.SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

        return response.message.content.strip()