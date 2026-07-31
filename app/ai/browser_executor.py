from app.browser.browser_agent import BrowserAgent


class BrowserExecutor:

    def execute(self, plan):

        steps = plan.get("steps", [])

        if not steps:
            print("[ERROR] No browser steps found.")
            return

        print("\n========== BROWSER EXECUTION ==========\n")

        success = 0
        failed = 0

        for index, step in enumerate(steps, start=1):

            tool = step.get("tool")

            print(f"[STEP {index}] {tool}")

            try:

                if tool == "browser_open":

                    BrowserAgent.open(step["url"])

                elif tool == "browser_title":

                    BrowserAgent.title()

                elif tool == "browser_current_url":

                    BrowserAgent.current_url()

                elif tool == "browser_extract_text":

                    selector = step.get("selector", "body")

                    BrowserAgent.extract_text(selector)

                elif tool == "browser_screenshot":

                    filename = step.get("filename", "browser.png")

                    BrowserAgent.screenshot(filename)

                elif tool == "browser_refresh":

                    BrowserAgent.refresh()

                elif tool == "browser_back":

                    BrowserAgent.back()

                elif tool == "browser_forward":

                    BrowserAgent.forward()

                elif tool == "browser_close":

                    BrowserAgent.close()

                else:

                    print(f"[WARNING] Unknown Tool : {tool}")

                    failed += 1

                    continue

                success += 1

            except Exception as e:

                failed += 1

                print(f"[ERROR] {e}")

        print("\n========== EXECUTION SUMMARY ==========")

        print(f"Total Steps : {len(steps)}")
        print(f"Successful : {success}")
        print(f"Failed : {failed}")

        print("\n========== DONE ==========\n")