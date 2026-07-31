from playwright.sync_api import sync_playwright
import os


class BrowserManager:

    _playwright = None
    _context = None
    _page = None

    @classmethod
    def start(cls):

        try:

            if (
                cls._playwright is not None
                and cls._context is not None
                and cls._page is not None
                and not cls._page.is_closed()
            ):
                return cls._page

        except Exception:
            pass

        cls.close()

        cls._playwright = sync_playwright().start()

        chrome_profile = r"D:\JarvisAI\data\chrome_profile"

        os.makedirs(chrome_profile, exist_ok=True)

        cls._context = cls._playwright.chromium.launch_persistent_context(
            user_data_dir=chrome_profile,
            channel="chrome",
            headless=False,
            slow_mo=200,
            viewport={"width": 1400, "height": 900},
        )

        if cls._context.pages:
            cls._page = cls._context.pages[0]
        else:
            cls._page = cls._context.new_page()

        print("[SUCCESS] Browser Started")

        return cls._page

    @classmethod
    def page(cls):

        try:

            if cls._page is None:
                return cls.start()

            if cls._page.is_closed():

                print("[INFO] Page Closed. Restarting Browser...")

                return cls.start()

            return cls._page

        except Exception:

            print("[INFO] Browser Invalid. Restarting...")

            return cls.start()

    @classmethod
    def close(cls):

        try:
            if cls._context:
                cls._context.close()
        except:
            pass

        try:
            if cls._playwright:
                cls._playwright.stop()
        except:
            pass

        cls._playwright = None
        cls._context = None
        cls._page = None

        print("[SUCCESS] Browser Closed")