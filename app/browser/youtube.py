from app.browser.browser_manager import BrowserManager


class YouTube:

    @staticmethod
    def open():

        page = BrowserManager.page()

        page.goto("https://www.youtube.com")

        page.wait_for_load_state()

        print("[SUCCESS] YouTube Opened")

    @staticmethod
    def search(query):

        page = BrowserManager.page()

        page.wait_for_selector("input[name='search_query']")

        page.fill("input[name='search_query']", query)

        page.keyboard.press("Enter")

        page.wait_for_load_state()

        print(f"[SUCCESS] Searched : {query}")

    @staticmethod
    def open_first_video():

        page = BrowserManager.page()

        page.wait_for_selector("a#video-title")

        page.locator("a#video-title").first.click()

        page.wait_for_load_state()

        print("[SUCCESS] First Video Opened")

    @staticmethod
    def pause():

        page = BrowserManager.page()

        page.keyboard.press("k")

        print("[SUCCESS] Video Paused")

    @staticmethod
    def play():

        page = BrowserManager.page()

        page.keyboard.press("k")

        print("[SUCCESS] Video Playing")

    @staticmethod
    def fullscreen():

        page = BrowserManager.page()

        page.keyboard.press("f")

        print("[SUCCESS] Fullscreen Enabled")