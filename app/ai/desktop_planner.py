import json
from ollama import chat


class DesktopPlanner:

    def create_plan(self, command):

        prompt = f"""
You are Jarvis AI Desktop Planner.

Convert the user's request into desktop actions.

Available Desktop Tools:

desktop_open_chrome
desktop_open_calculator
desktop_open_notepad
desktop_open_vscode

Rules:
- Return ONLY valid JSON.
- No explanation.

Example:

{{
    "steps":[
        {{
            "tool":"desktop_open_calculator"
        }}
    ]
}}

User Request:
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

        raw = response["message"]["content"].strip()

        print("\n[RAW PLAN]")
        print(raw)

        try:
            return json.loads(raw)
        except Exception:
            print("[ERROR] Invalid JSON")
            return {"steps": []}