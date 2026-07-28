from app.browser.browser_manager import BrowserManager


class GoogleSearch:

    @staticmethod
    def search(query):

        page = BrowserManager.page()

        page.goto("https://www.google.com")

        page.wait_for_load_state("domcontentloaded")

        try:
            page.locator("button:has-text('Accept all')").click(timeout=2000)
        except:
            pass

        page.wait_for_selector("textarea[name='q']")

        page.fill("textarea[name='q']", query)

        page.keyboard.press("Enter")

        page.wait_for_load_state("networkidle")

        print(f"[SUCCESS] Google Search: {query}")

    @staticmethod
    def open_first_result():

        page = BrowserManager.page()

        page.wait_for_timeout(3000)

        # Multiple selectors try karo
        selectors = [
            "a:has(h3)",
            "div.yuRUbf > a",
            "h3 >> xpath=..",
            "a[jsname]",
            "a[href^='http']"
        ]

        for selector in selectors:

            try:
                links = page.locator(selector)

                if links.count() > 0:

                    print(f"[FOUND] {selector}")

                    links.first.click(timeout=5000)

                    page.wait_for_load_state("networkidle")

                    print("[SUCCESS] First Result Opened")

                    return

            except:
                pass

        print("[ERROR] No Search Results Found")

        page.screenshot(path="google_error.png")

        print("[INFO] Screenshot Saved : google_error.png")

    @staticmethod
    def get_title():

        page = BrowserManager.page()

        print(page.title())

        return page.title()

    @staticmethod
    def current_url():

        page = BrowserManager.page()

        print(page.url)

        return page.url