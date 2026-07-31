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

        except Exception as e:

            print(f"[WARNING] {e}")
            print("[INFO] Restarting Browser...")

            page = BrowserManager.start()

            page.reload(wait_until="domcontentloaded")

        print("[SUCCESS] Page Refreshed")

    @staticmethod
    def back():

        try:

            page = BrowserManager.page()

            page.go_back(wait_until="domcontentloaded")

        except Exception as e:

            print(f"[WARNING] {e}")
            print("[INFO] Restarting Browser...")

            page = BrowserManager.start()

            page.go_back(wait_until="domcontentloaded")

        print("[SUCCESS] Back")

    @staticmethod
    def forward():

        try:

            page = BrowserManager.page()

            page.go_forward(wait_until="domcontentloaded")

        except Exception as e:

            print(f"[WARNING] {e}")
            print("[INFO] Restarting Browser...")

            page = BrowserManager.start()

            page.go_forward(wait_until="domcontentloaded")

        print("[SUCCESS] Forward")

    @staticmethod
    def title():

        try:

            page = BrowserManager.page()

            title = page.title()

        except Exception as e:

            print(f"[WARNING] {e}")
            print("[INFO] Restarting Browser...")

            page = BrowserManager.start()

            title = page.title()

        print(f"[TITLE] {title}")

        return title

    @staticmethod
    def current_url():

        try:

            page = BrowserManager.page()

            url = page.url

        except Exception as e:

            print(f"[WARNING] {e}")
            print("[INFO] Restarting Browser...")

            page = BrowserManager.start()

            url = page.url

        print(f"[URL] {url}")

        return url

    @staticmethod
    def screenshot(filename="screenshot.png"):

        try:

            page = BrowserManager.page()

            page.screenshot(path=filename)

        except Exception as e:

            print(f"[WARNING] {e}")
            print("[INFO] Restarting Browser...")

            page = BrowserManager.start()

            page.screenshot(path=filename)

        print(f"[SUCCESS] Screenshot Saved : {filename}")

    @staticmethod
    def close():

        BrowserManager.close()