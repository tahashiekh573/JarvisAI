from playwright.sync_api import sync_playwright
import os


class BrowserManager:

    _playwright = None
    _browser = None
    _context = None
    _page = None

    PROFILE = r"D:\JarvisAI\data\chrome_profile"

    @classmethod
    def start(cls):

        try:
            if cls._page and not cls._page.is_closed():
                return cls._page
        except Exception:
            pass

        os.makedirs(cls.PROFILE, exist_ok=True)

        if cls._playwright is None:
            cls._playwright = sync_playwright().start()

        # Browser
        if cls._browser is None:

            cls._browser = cls._playwright.chromium.launch(
                channel="chrome",
                headless=False,
                slow_mo=150
            )

        # Context
        if cls._context is None:

            cls._context = cls._browser.new_context(
                ignore_https_errors=True,
                viewport={
                    "width": 1400,
                    "height": 900
                }
            )

        # Page
        if cls._page is None or cls._page.is_closed():

            cls._page = cls._context.new_page()
            cls._page.set_default_timeout(30000)

        print("[SUCCESS] Browser Started")

        return cls._page

    @classmethod
    def page(cls):

        try:

            if cls._page is None:
                return cls.start()

            if cls._page.is_closed():

                cls._page = cls._context.new_page()
                cls._page.set_default_timeout(30000)

            return cls._page

        except Exception:

            return cls.restart()

    @classmethod
    def restart(cls):

        print("[INFO] Restarting Browser...")

        try:
            if cls._page:
                cls._page.close()
        except Exception:
            pass

        cls._page = None

        return cls.start()

    @classmethod
    def close(cls):

        try:
            if cls._context:
                cls._context.close()
        except Exception:
            pass

        try:
            if cls._browser:
                cls._browser.close()
        except Exception:
            pass

        try:
            if cls._playwright:
                cls._playwright.stop()
        except Exception:
            pass

        cls._page = None
        cls._context = None
        cls._browser = None
        cls._playwright = None

        print("[SUCCESS] Browser Closed")