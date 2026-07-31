import json
from ollama import chat


class BrowserPlanner:

    def create_plan(self, command):

        prompt = f"""
You are Jarvis Browser Planner.

Your job is to convert the user's request into browser actions.

Available Browser Tools:

1. browser_open
   Parameters:
   - url

2. browser_title

3. browser_current_url

4. browser_extract_text
   Parameters:
   - selector

5. browser_screenshot
   Optional Parameters:
   - filename

6. browser_refresh

7. browser_back

8. browser_forward

9. browser_close

=========================
Rules
=========================

1. Return ONLY valid JSON.
2. Do NOT write explanations.
3. Do NOT use markdown.
4. Always return this format:

{{
    "steps":[
        {{
            "tool":"browser_open",
            "url":"https://example.com"
        }}
    ]
}}

5. If browser_extract_text is used,
ALWAYS provide a selector.

Common selectors:

Heading:
"h1"

Sub Heading:
"h2"

Paragraph:
"p"

Entire Page:
"body"

=========================
Examples
=========================

User:
Open python.org

Output:

{{
    "steps":[
        {{
            "tool":"browser_open",
            "url":"https://python.org"
        }}
    ]
}}

-------------------------

User:
Open python.org and read the heading

Output:

{{
    "steps":[
        {{
            "tool":"browser_open",
            "url":"https://python.org"
        }},
        {{
            "tool":"browser_extract_text",
            "selector":"h1"
        }}
    ]
}}

-------------------------

User:
Open python.org and read first paragraph

Output:

{{
    "steps":[
        {{
            "tool":"browser_open",
            "url":"https://python.org"
        }},
        {{
            "tool":"browser_extract_text",
            "selector":"p"
        }}
    ]
}}

-------------------------

User:
Open example.com then take screenshot then close browser

Output:

{{
    "steps":[
        {{
            "tool":"browser_open",
            "url":"https://example.com"
        }},
        {{
            "tool":"browser_screenshot",
            "filename":"example.png"
        }},
        {{
            "tool":"browser_close"
        }}
    ]
}}

=========================

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

        # Remove markdown if model accidentally returns it
        raw = raw.replace("```json", "").replace("```", "").strip()

        try:
            plan = json.loads(raw)

            if "steps" not in plan:
                print("[ERROR] Missing 'steps' key.")
                return {"steps": []}

            return plan

        except json.JSONDecodeError as e:

            print(f"[ERROR] Invalid JSON: {e}")

            return {"steps": []}