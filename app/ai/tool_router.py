from ollama import chat


class ToolRouter:

    def route(self, command):

        prompt = f"""
You are Jarvis AI.

Your job is to decide which planner should handle the user's request.

Available planners:

desktop
browser
whatsapp
file
unknown

Rules:

- Opening websites -> browser
- Search on internet -> browser
- Read webpage -> browser
- Browser actions -> browser

- Open calculator -> desktop
- Open chrome application -> desktop
- Open VS Code -> desktop
- Open notepad -> desktop

- Send WhatsApp message -> whatsapp

- Read file -> file
- Open pdf -> file

Return ONLY one word.

User:
{command}
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

        planner = response["message"]["content"].strip().lower()

        print(f"[ROUTER] {planner}")

        return planner