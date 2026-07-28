from playwright.sync_api import sync_playwright


class BrowserManager:
    """
    Singleton Browser Manager

    Sirf ek browser instance poori application me use hoga.
    """

    _playwright = None
    _browser = None
    _page = None

    @classmethod
    def start(cls):
        """
        Launch Chromium Browser
        """

        if cls._browser is None:

            cls._playwright = sync_playwright().start()

            cls._browser = cls._playwright.chromium.launch(
                headless=False,
                slow_mo=200
            )

            cls._page = cls._browser.new_page()

            print("[SUCCESS] Browser Started")

        return cls._page

    @classmethod
    def page(cls):

        if cls._page is None:
            return cls.start()

        return cls._page

    @classmethod
    def close(cls):

        if cls._browser:

            cls._browser.close()

            cls._playwright.stop()

            cls._browser = None
            cls._playwright = None
            cls._page = None

            print("[SUCCESS] Browser Closed")