from app.browser.chrome import Chrome
import time


class BrowserAgent:

    @staticmethod
    def open(url):
        print(f"[BROWSER] Opening : {url}")
        Chrome.open(url)

    @staticmethod
    def title():
        return Chrome.title()

    @staticmethod
    def current_url():
        return Chrome.current_url()

    @staticmethod
    def screenshot(filename="screenshot.png"):
        try:
            Chrome.screenshot(filename)
        except Exception as e:
            print(f"[ERROR] Screenshot Failed : {e}")

    @staticmethod
    def refresh():
        Chrome.refresh()

    @staticmethod
    def back():
        Chrome.back()

    @staticmethod
    def forward():
        Chrome.forward()

    @staticmethod
    def click(selector):

        page = Chrome.page()

        try:

            locator = page.locator(selector).first

            locator.wait_for(timeout=5000)

            locator.click()

            print(f"[SUCCESS] Clicked : {selector}")

        except Exception as e:

            print(f"[ERROR] Click Failed : {e}")

    @staticmethod
    def type(selector, text):

        page = Chrome.page()

        try:

            locator = page.locator(selector).first

            locator.wait_for(timeout=5000)

            locator.fill(text)

            print(f"[SUCCESS] Typed : {text}")

        except Exception as e:

            print(f"[ERROR] Type Failed : {e}")

    @staticmethod
    def press(key):

        page = Chrome.page()

        try:

            page.keyboard.press(key)

            print(f"[SUCCESS] Key Pressed : {key}")

        except Exception as e:

            print(f"[ERROR] Key Press Failed : {e}")

    @staticmethod
    def wait(seconds):

        print(f"[WAIT] {seconds} second(s)")

        time.sleep(seconds)

    @staticmethod
    def extract_text(selector="body"):

        page = Chrome.page()

        try:

            locator = page.locator(selector)

            if locator.count() == 0:

                print(f"[ERROR] Element Not Found : {selector}")

                return ""

            locator.first.wait_for(timeout=5000)

            text = locator.first.inner_text().strip()

            print(f"[TEXT]\n{text}")

            return text

        except Exception as e:

            print(f"[ERROR] Extract Failed : {e}")

            return ""

    @staticmethod
    def exists(selector):

        page = Chrome.page()

        try:

            return page.locator(selector).count() > 0

        except Exception:

            return False

    @staticmethod
    def wait_for(selector, timeout=5000):

        page = Chrome.page()

        try:

            page.wait_for_selector(
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

        page = Chrome.page()

        try:

            locator = page.locator(selector)

            if locator.count() == 0:
                return ""

            return locator.first.text_content()

        except Exception:

            return ""

    @staticmethod
    def html(selector="body"):

        page = Chrome.page()

        try:

            return page.locator(selector).first.inner_html()

        except Exception:

            return ""

    @staticmethod
    def close():

        Chrome.close()