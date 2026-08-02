from urllib.parse import quote_plus
from app.browser.chrome import Chrome


class DuckDuckGo:

    @staticmethod
    def search(query):

        try:

            url = f"https://duckduckgo.com/?q={quote_plus(query)}"

            if not Chrome.open(url):
                return False

            page = Chrome.page()

            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(2000)

            print(f"[SEARCH] {query}")

            return True

        except Exception as e:

            print(f"[ERROR] Search Failed : {e}")

            return False

    @staticmethod
    def open_first_result():

        try:

            page = Chrome.page()

            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(2000)

            selectors = [

                "a[data-testid='result-title-a']",

                "article[data-testid='result'] a[data-testid='result-title-a']",

                "article h2 a",

                "article a[href]",

                "h2 a",

                "a[href]"

            ]

            for selector in selectors:

                try:

                    locator = page.locator(selector).first

                    locator.wait_for(
                        state="visible",
                        timeout=5000
                    )

                    href = locator.get_attribute("href")

                    if not href:
                        continue

                    if href.startswith("#"):
                        continue

                    if "duckduckgo.com" in href and "uddg=" not in href:
                        continue

                    locator.scroll_into_view_if_needed()

                    locator.click()

                    page.wait_for_load_state("domcontentloaded")
                    page.wait_for_timeout(2000)

                    print("[SUCCESS] First Result Opened")

                    return True

                except Exception:
                    continue

            print("[ERROR] No Search Result Found")

            return False

        except Exception as e:

            print(f"[ERROR] {e}")

            return False

    @staticmethod
    def search_and_open(query):

        if DuckDuckGo.search(query):
            return DuckDuckGo.open_first_result()

        return False

    @staticmethod
    def search_images(query):

        try:

            url = f"https://duckduckgo.com/?q={quote_plus(query)}&iax=images&ia=images"

            if not Chrome.open(url):
                return False

            page = Chrome.page()

            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(2000)

            print("[SUCCESS] Images Opened")

            return True

        except Exception as e:

            print(f"[ERROR] Images Search Failed : {e}")

            return False

    @staticmethod
    def search_news(query):

        try:

            url = f"https://duckduckgo.com/?q={quote_plus(query)}&iar=news&ia=news"

            if not Chrome.open(url):
                return False

            page = Chrome.page()

            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(2000)

            print("[SUCCESS] News Opened")

            return True

        except Exception as e:

            print(f"[ERROR] News Search Failed : {e}")

            return False