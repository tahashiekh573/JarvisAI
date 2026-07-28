from app.browser.browser_manager import BrowserManager


class Chrome:

    @staticmethod
    def open(url="https://www.google.com"):

        page = BrowserManager.page()

        page.goto(url)

        print(f"[SUCCESS] Opened: {url}")


    @staticmethod
    def refresh():

        page = BrowserManager.page()

        page.reload()

        print("[SUCCESS] Page Refreshed")


    @staticmethod
    def back():

        page = BrowserManager.page()

        page.go_back()

        print("[SUCCESS] Back")


    @staticmethod
    def forward():

        page = BrowserManager.page()

        page.go_forward()

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