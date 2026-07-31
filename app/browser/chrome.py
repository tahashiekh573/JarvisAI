from app.browser.browser_manager import BrowserManager


class Chrome:

    @staticmethod
    def page():
        return BrowserManager.page()

    @staticmethod
    def open(url="https://www.google.com"):

        try:

            page = BrowserManager.page()

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=30000
            )

        except Exception as e:

            print(f"[WARNING] {e}")
            print("[INFO] Restarting Browser...")

            BrowserManager.close()

            page = BrowserManager.start()

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=30000
            )

        print(f"[SUCCESS] Opened: {url}")

    @staticmethod
    def refresh():

        try:

            page = BrowserManager.page()

            page.reload(wait_until="domcontentloaded")

            print("[SUCCESS] Page Refreshed")

        except Exception:

            print("[INFO] Restarting Browser...")

            BrowserManager.start()

    @staticmethod
    def back():

        page = BrowserManager.page()

        page.go_back(wait_until="domcontentloaded")

        print("[SUCCESS] Back")

    @staticmethod
    def forward():

        page = BrowserManager.page()

        page.go_forward(wait_until="domcontentloaded")

        print("[SUCCESS] Forward")

    @staticmethod
    def title():

        page = BrowserManager.page()

        title = page.title()

        print(f"[TITLE] {title}")

        return title

    @staticmethod
    def current_url():

        page = BrowserManager.page()

        url = page.url

        print(f"[URL] {url}")

        return url

    @staticmethod
    def screenshot(filename="screenshot.png"):

        page = BrowserManager.page()

        page.screenshot(path=filename)

        print(f"[SUCCESS] Screenshot Saved : {filename}")

    @staticmethod
    def close():

        BrowserManager.close()