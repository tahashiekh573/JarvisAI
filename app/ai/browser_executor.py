from app.browser.browser_agent import BrowserAgent


class BrowserExecutor:

    def execute(self, plan):

        steps = plan.get("steps", [])

        if not steps:
            print("[ERROR] No browser steps found.")
            return False

        print("\n========== BROWSER EXECUTION ==========\n")

        success = 0
        failed = 0

        for index, step in enumerate(steps, start=1):

            tool = step.get("tool")

            print(f"[STEP {index}] {tool}")

            result = False

            try:

                # ======================================
                # Browser
                # ======================================

                if tool == "browser_open":

                    result = BrowserAgent.open(step["url"])

                elif tool == "browser_title":

                    title = BrowserAgent.title()

                    if title:
                        print(f"[TITLE] {title}")
                        result = True

                elif tool == "browser_current_url":

                    url = BrowserAgent.current_url()

                    if url:
                        print(f"[URL] {url}")
                        result = True

                elif tool == "browser_extract_text":

                    selector = step.get("selector", "body")

                    text = BrowserAgent.extract_text(selector)

                    result = bool(text)

                elif tool == "browser_screenshot":

                    filename = step.get("filename", "browser.png")

                    result = BrowserAgent.screenshot(filename)

                elif tool == "browser_refresh":

                    result = BrowserAgent.refresh()

                elif tool == "browser_back":

                    result = BrowserAgent.back()

                elif tool == "browser_forward":

                    result = BrowserAgent.forward()

                elif tool == "browser_close":

                    result = BrowserAgent.close()

                # ======================================
                # DuckDuckGo
                # ======================================

                elif tool == "browser_search":

                    result = BrowserAgent.search(step["query"])

                elif tool == "browser_open_first_result":

                    result = BrowserAgent.open_first_result()

                elif tool == "browser_search_and_open":

                    result = BrowserAgent.search_and_open(step["query"])

                elif tool == "browser_search_images":

                    result = BrowserAgent.search_images(step["query"])

                elif tool == "browser_search_news":

                    result = BrowserAgent.search_news(step["query"])

                else:

                    print(f"[WARNING] Unknown Tool: {tool}")
                    failed += 1
                    continue

                if result:
                    success += 1
                else:
                    failed += 1

            except Exception as e:

                failed += 1
                print(f"[ERROR] {e}")

        print("\n========== EXECUTION SUMMARY ==========")
        print(f"Total Steps : {len(steps)}")
        print(f"Successful : {success}")
        print(f"Failed : {failed}")
        print("\n========== DONE ==========\n")

        return failed == 0