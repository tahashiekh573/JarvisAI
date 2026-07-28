from playwright.sync_api import sync_playwright
import os


class BrowserManager:
    """
    Singleton Browser Manager
    """

    _playwright = None
    _context = None
    _page = None

    @classmethod
    def start(cls):

        if cls._context is None:

            cls._playwright = sync_playwright().start()

            # Jarvis ka apna Chrome Profile
            chrome_profile = r"D:\JarvisAI\data\chrome_profile"

            # Folder create agar exist nahi karta
            os.makedirs(chrome_profile, exist_ok=True)

            cls._context = cls._playwright.chromium.launch_persistent_context(
                user_data_dir=chrome_profile,
                channel="chrome",
                headless=False,
                slow_mo=200,
                viewport={"width": 1400, "height": 900},
            )

            # Existing page use karo
            if cls._context.pages:
                cls._page = cls._context.pages[0]
            else:
                cls._page = cls._context.new_page()

            print("[SUCCESS] Browser Started")

        return cls._page

    @classmethod
    def page(cls):

        if cls._page is None:
            return cls.start()

        return cls._page

    @classmethod
    def close(cls):

        if cls._context:

            cls._context.close()

            cls._playwright.stop()

            cls._context = None
            cls._playwright = None
            cls._page = None

            print("[SUCCESS] Browser Closed")