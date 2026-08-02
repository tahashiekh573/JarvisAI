from app.browser.browser_manager import BrowserManager
from playwright._impl._errors import TargetClosedError


class Chrome:

    @staticmethod
    def page():
        return BrowserManager.page()

    @staticmethod
    def _alive_page():
        page = BrowserManager.page()

        if page.is_closed():
            raise TargetClosedError("Page Closed")

        return page

    @staticmethod
    def open(url):

        try:

            page = Chrome._alive_page()

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(1000)

            print(f"[SUCCESS] Opened: {url}")

            return True

        except TargetClosedError:

            print("[INFO] Restarting Browser...")

            page = BrowserManager.restart()

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(1000)

            print(f"[SUCCESS] Opened: {url}")

            return True

        except Exception as e:

            print(f"[ERROR] {e}")

            return False

    @staticmethod
    def refresh():

        try:

            Chrome._alive_page().reload(wait_until="domcontentloaded")

            print("[SUCCESS] Refreshed")

            return True

        except TargetClosedError:

            BrowserManager.restart().reload()

            return True

        except Exception as e:

            print(e)

            return False

    @staticmethod
    def back():

        try:

            Chrome._alive_page().go_back()

            print("[SUCCESS] Back")

            return True

        except TargetClosedError:

            BrowserManager.restart()

            return False

        except Exception as e:

            print(e)

            return False

    @staticmethod
    def forward():

        try:

            Chrome._alive_page().go_forward()

            print("[SUCCESS] Forward")

            return True

        except TargetClosedError:

            BrowserManager.restart()

            return False

        except Exception as e:

            print(e)

            return False

    @staticmethod
    def title():

        try:
            return Chrome._alive_page().title()

        except:
            return ""

    @staticmethod
    def current_url():

        try:
            return Chrome._alive_page().url

        except:
            return ""

    @staticmethod
    def screenshot(filename="screenshot.png"):

        try:

            Chrome._alive_page().screenshot(path=filename)

            print("[SUCCESS] Screenshot Saved")

            return True

        except TargetClosedError:

            BrowserManager.restart().screenshot(path=filename)

            return True

        except Exception as e:

            print(e)

            return False

    @staticmethod
    def close():

        BrowserManager.close()

        return True