from app.browser.chrome import Chrome
from app.browser.duckduckgo import DuckDuckGo
import time


class BrowserAgent:

    # ======================================
    # BASIC BROWSER
    # ======================================

    @staticmethod
    def open(url):
        print(f"[BROWSER] Opening : {url}")
        return Chrome.open(url)

    @staticmethod
    def title():
        return Chrome.title()

    @staticmethod
    def current_url():
        return Chrome.current_url()

    @staticmethod
    def screenshot(filename="screenshot.png"):
        return Chrome.screenshot(filename)

    @staticmethod
    def refresh():
        return Chrome.refresh()

    @staticmethod
    def back():
        return Chrome.back()

    @staticmethod
    def forward():
        return Chrome.forward()

    # ======================================
    # ELEMENT ACTIONS
    # ======================================

    @staticmethod
    def click(selector):

        try:

            page = Chrome.page()

            locator = page.locator(selector).first

            locator.wait_for(state="visible", timeout=5000)

            locator.click()

            print(f"[SUCCESS] Clicked : {selector}")

            return True

        except Exception as e:

            print(f"[ERROR] Click Failed : {e}")

            return False

    @staticmethod
    def type(selector, text):

        try:

            page = Chrome.page()

            locator = page.locator(selector).first

            locator.wait_for(state="visible", timeout=5000)

            locator.fill(text)

            print(f"[SUCCESS] Typed : {text}")

            return True

        except Exception as e:

            print(f"[ERROR] Type Failed : {e}")

            return False

    @staticmethod
    def press(key):

        try:

            Chrome.page().keyboard.press(key)

            print(f"[SUCCESS] Key Pressed : {key}")

            return True

        except Exception as e:

            print(f"[ERROR] Key Press Failed : {e}")

            return False

    @staticmethod
    def wait(seconds):

        print(f"[WAIT] {seconds} second(s)")

        time.sleep(seconds)

    # ======================================
    # CONTENT
    # ======================================

    @staticmethod
    def extract_text(selector="body"):

        try:

            page = Chrome.page()

            locator = page.locator(selector)

            if locator.count() == 0:

                print(f"[ERROR] Element Not Found : {selector}")

                return ""

            locator.first.wait_for(state="visible", timeout=5000)

            text = locator.first.inner_text().strip()

            print(f"[TEXT]\n{text}")

            return text

        except Exception as e:

            print(f"[ERROR] Extract Failed : {e}")

            return ""

    @staticmethod
    def exists(selector):

        try:

            return Chrome.page().locator(selector).count() > 0

        except Exception:

            return False

    @staticmethod
    def wait_for(selector, timeout=5000):

        try:

            Chrome.page().wait_for_selector(
                selector,
                timeout=timeout,
                state="visible"
            )

            print(f"[SUCCESS] Found : {selector}")

            return True

        except Exception:

            print(f"[ERROR] Timeout : {selector}")

            return False

    @staticmethod
    def text_content(selector):

        try:

            locator = Chrome.page().locator(selector)

            if locator.count() == 0:
                return ""

            return locator.first.text_content()

        except Exception:

            return ""

    @staticmethod
    def html(selector="body"):

        try:

            return Chrome.page().locator(selector).first.inner_html()

        except Exception:

            return ""

    # ======================================
    # DUCKDUCKGO
    # ======================================

    @staticmethod
    def search(query):
        return DuckDuckGo.search(query)

    @staticmethod
    def open_first_result():
        return DuckDuckGo.open_first_result()

    @staticmethod
    def search_and_open(query):
        return DuckDuckGo.search_and_open(query)

    @staticmethod
    def search_images(query):
        return DuckDuckGo.search_images(query)

    @staticmethod
    def search_news(query):
        return DuckDuckGo.search_news(query)

    # ======================================
    # CLOSE
    # ======================================

    @staticmethod
    def close():
        return Chrome.close()