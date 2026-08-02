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
Rules
==============================

1. Return ONLY valid JSON.
2. No markdown.
3. No explanation.
4. Start with {{
5. End with }}
6. Always return:

{{
    "steps":[]
}}

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
Search Python Tutorial

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

Selectors

Heading
"h1"

Sub Heading
"h2"

Paragraph
"p"

Whole Page
"body"

==============================

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
                return {"steps": []}

            if "steps" not in plan:
                return {"steps": []}

            if not isinstance(plan["steps"], list):
                return {"steps": []}

            return plan

        except Exception as e:

            print("[ERROR]", e)
            print(raw)

            return {"steps": []}