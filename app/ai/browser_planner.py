import json
import re
from ollama import chat


class BrowserPlanner:

    def create_plan(self, command):

        prompt = f"""
You are Jarvis Browser Planner.

Your job is to convert the user's request into browser actions.

Return ONLY valid JSON.

Never explain.
Never use markdown.
Never use ```.

Response MUST start with {{
Response MUST end with }}

==================================
Available Browser Tools
==================================

browser_open
url

browser_title

browser_current_url

browser_refresh

browser_back

browser_forward

browser_close

browser_screenshot
filename (optional)

browser_extract_text
selector

browser_read_page

browser_read_heading

browser_read_article

browser_search
query

browser_open_first_result

browser_search_and_open
query

browser_search_images
query

browser_search_news
query

==================================
Rules
==================================

Return ONLY

{{
    "steps":[]
}}

----------------------------------

Search OpenAI

{{
 "steps":[
   {{
      "tool":"browser_search",
      "query":"OpenAI"
   }}
 ]
}}

----------------------------------

Search OpenAI and open first result

{{
 "steps":[
   {{
      "tool":"browser_search",
      "query":"OpenAI"
   }},
   {{
      "tool":"browser_open_first_result"
   }}
 ]
}}

----------------------------------

Search AI images

{{
 "steps":[
   {{
      "tool":"browser_search_images",
      "query":"AI"
   }}
 ]
}}

----------------------------------

Search AI news

{{
 "steps":[
   {{
      "tool":"browser_search_news",
      "query":"AI"
   }}
 ]
}}

----------------------------------

Open github.com

{{
 "steps":[
   {{
      "tool":"browser_open",
      "url":"https://github.com"
   }}
 ]
}}

----------------------------------

Read page

{{
 "steps":[
   {{
      "tool":"browser_read_page"
   }}
 ]
}}

----------------------------------

Read heading

{{
 "steps":[
   {{
      "tool":"browser_read_heading"
   }}
 ]
}}

----------------------------------

Read article

{{
 "steps":[
   {{
      "tool":"browser_read_article"
   }}
 ]
}}

----------------------------------

Open python.org and read heading

{{
 "steps":[
   {{
      "tool":"browser_open",
      "url":"https://python.org"
   }},
   {{
      "tool":"browser_read_heading"
   }}
 ]
}}

----------------------------------

Open python.org and read page

{{
 "steps":[
   {{
      "tool":"browser_open",
      "url":"https://python.org"
   }},
   {{
      "tool":"browser_read_page"
   }}
 ]
}}

----------------------------------

What is page title

{{
 "steps":[
   {{
      "tool":"browser_title"
   }}
 ]
}}

----------------------------------

Current URL

{{
 "steps":[
   {{
      "tool":"browser_current_url"
   }}
 ]
}}

----------------------------------

Take screenshot

{{
 "steps":[
   {{
      "tool":"browser_screenshot"
   }}
 ]
}}

----------------------------------

Refresh

{{
 "steps":[
   {{
      "tool":"browser_refresh"
   }}
 ]
}}

----------------------------------

Back

{{
 "steps":[
   {{
      "tool":"browser_back"
   }}
 ]
}}

----------------------------------

Forward

{{
 "steps":[
   {{
      "tool":"browser_forward"
   }}
 ]
}}

----------------------------------

Close browser

{{
 "steps":[
   {{
      "tool":"browser_close"
   }}
 ]
}}

==================================

Important

Never convert

read page

into browser_search.

Never convert

read heading

into browser_search.

Never convert

read article

into browser_search.

Use browser_read_page,
browser_read_heading,
browser_read_article directly.

Only use browser_search when user explicitly says SEARCH.

==================================

User Request

{command}
"""

        response = chat(
            model="llama3.2:3b",
            options={
                "temperature": 0,
                "top_p": 0.1,
                "num_predict": 200
            },
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Return ONLY valid JSON. "
                        "No explanation. "
                        "No markdown. "
                        "No text before JSON. "
                        "No text after JSON."
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
        raw = raw.replace("```", "").strip()

        match = re.search(r"\{.*\}", raw, re.DOTALL)

        if match:
            raw = match.group(0)

        try:

            plan = json.loads(raw)

            if not isinstance(plan, dict):
                raise Exception()

            if "steps" not in plan:
                raise Exception()

            if not isinstance(plan["steps"], list):
                raise Exception()

            return plan

        except Exception:

            print("[ERROR] Invalid planner output")

            return {
                "steps": []
            }