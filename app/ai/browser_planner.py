import json
import re
from ollama import chat


class BrowserPlanner:

    def create_plan(self, command):

        prompt = f"""
You are Jarvis Browser Planner.

Convert the user's request into browser actions.

==============================
Available Browser Tools
==============================

browser_open
Parameters:
url

browser_title

browser_current_url

browser_extract_text
Parameters:
selector

browser_screenshot
Optional:
filename

browser_refresh

browser_back

browser_forward

browser_close

browser_search
Parameters:
query

browser_open_first_result

browser_search_and_open
Parameters:
query

browser_search_images
Parameters:
query

browser_search_news
Parameters:
query

==============================
IMPORTANT RULES
==============================

1. Return ONLY valid JSON.
2. Never explain.
3. Never use markdown.
4. Never write ```json.
5. Never write text before JSON.
6. Never write text after JSON.
7. Response MUST start with {{
8. Response MUST end with }}

Only return:

{{
    "steps":[]
}}

Search Rules

If user says:

Search OpenAI

Return

{{
    "steps":[
        {{
            "tool":"browser_search",
            "query":"OpenAI"
        }}
    ]
}}

Do NOT automatically open first result.

Open first result ONLY when user explicitly says

- open first result
- open first link
- visit first result
- go to first result

Selectors

Heading:
"h1"

Sub Heading:
"h2"

Paragraph:
"p"

Whole Page:
"body"

==============================
Examples
==============================

User:
Open python.org

Output

{{
    "steps":[
        {{
            "tool":"browser_open",
            "url":"https://python.org"
        }}
    ]
}}

-----------------------------

User:
Open python.org and read heading

Output

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

-----------------------------

User:
Search ChatGPT

Output

{{
    "steps":[
        {{
            "tool":"browser_search",
            "query":"ChatGPT"
        }}
    ]
}}

-----------------------------

User:
Search Python Tutorial and open first result

Output

{{
    "steps":[
        {{
            "tool":"browser_search",
            "query":"Python Tutorial"
        }},
        {{
            "tool":"browser_open_first_result"
        }}
    ]
}}

-----------------------------

User:
Search OpenAI then read page

Output

{{
    "steps":[
        {{
            "tool":"browser_search",
            "query":"OpenAI"
        }},
        {{
            "tool":"browser_open_first_result"
        }},
        {{
            "tool":"browser_extract_text",
            "selector":"body"
        }}
    ]
}}

-----------------------------

User:
Search AI Images

Output

{{
    "steps":[
        {{
            "tool":"browser_search_images",
            "query":"AI"
        }}
    ]
}}

-----------------------------

User:
Search AI News

Output

{{
    "steps":[
        {{
            "tool":"browser_search_news",
            "query":"AI"
        }}
    ]
}}

==============================

User Request:

{command}
"""

        response = chat(
            model="llama3.2:3b",
            options={
                "temperature": 0,
                "num_predict": 256
            },
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a JSON generator. "
                        "Return ONLY valid JSON. "
                        "Never explain anything. "
                        "Never use markdown. "
                        "Never write text before JSON. "
                        "Never write text after JSON."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        raw = response["message"]["content"]

        print("\n[RAW PLAN]")
        print(raw)

        raw = raw.replace("```json", "")
        raw = raw.replace("```", "")
        raw = raw.strip()

        match = re.search(r"\{.*\}", raw, re.DOTALL)

        if match:
            raw = match.group(0)

        try:

            plan = json.loads(raw)

            if not isinstance(plan, dict):
                raise ValueError("Planner returned non-object JSON")

            if "steps" not in plan:
                raise ValueError("'steps' key missing")

            if not isinstance(plan["steps"], list):
                raise ValueError("'steps' must be a list")

            return plan

        except Exception as e:

            print(f"[ERROR] Invalid Planner Output: {e}")
            print(raw)

            return {
                "steps": []
            }