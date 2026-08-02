from app.browser.chrome import Chrome


class PageReader:

    @staticmethod
    def _page():
        return Chrome.page()

    # ==========================================
    # READ HEADING
    # h1 -> h2 -> title
    # ==========================================

    @staticmethod
    def read_heading():

        page = PageReader._page()

        selectors = [
            "h1",
            "main h1",
            "article h1",
            "h2",
            "main h2",
            "article h2"
        ]

        for selector in selectors:

            try:

                locator = page.locator(selector)

                if locator.count() > 0:

                    text = locator.first.inner_text().strip()

                    if text:

                        print(f"[HEADING]\n{text}")

                        return text

            except:
                pass

        try:

            title = page.title()

            print(f"[TITLE]\n{title}")

            return title

        except:
            pass

        print("[ERROR] Heading Not Found")

        return ""

    # ==========================================
    # READ ARTICLE
    # ==========================================

    @staticmethod
    def read_article():

        page = PageReader._page()

        selectors = [

            "article",

            "main",

            "[role='main']",

            ".content",

            ".post",

            ".article",

            "#content",

            "body"

        ]

        for selector in selectors:

            try:

                locator = page.locator(selector)

                if locator.count() == 0:
                    continue

                text = locator.first.inner_text().strip()

                if len(text) > 100:

                    print("[ARTICLE]\n")
                    print(text)

                    return text

            except:
                pass

        print("[ERROR] Article Not Found")

        return ""

    # ==========================================
    # READ PAGE
    # ==========================================

    @staticmethod
    def read_page():

        page = PageReader._page()

        selectors = [

            "main",

            "article",

            "[role='main']",

            "body"

        ]

        for selector in selectors:

            try:

                locator = page.locator(selector)

                if locator.count() == 0:
                    continue

                text = locator.first.inner_text().strip()

                if text:

                    print("[TEXT]\n")
                    print(text)

                    return text

            except:
                pass

        print("[ERROR] Page Empty")

        return ""

    # ==========================================
    # LINKS
    # ==========================================

    @staticmethod
    def extract_links():

        page = PageReader._page()

        try:

            links = page.locator("a")

            result = []

            count = links.count()

            for i in range(count):

                try:

                    a = links.nth(i)

                    href = a.get_attribute("href")
                    text = a.inner_text().strip()

                    if href:

                        result.append({

                            "text": text,

                            "url": href

                        })

                except:
                    pass

            print(f"[LINKS] {len(result)} Found")

            for item in result:

                print(item)

            return result

        except Exception as e:

            print(e)

            return []

    # ==========================================
    # IMAGES
    # ==========================================

    @staticmethod
    def extract_images():

        page = PageReader._page()

        try:

            imgs = page.locator("img")

            result = []

            count = imgs.count()

            for i in range(count):

                try:

                    img = imgs.nth(i)

                    result.append({

                        "src": img.get_attribute("src"),

                        "alt": img.get_attribute("alt")

                    })

                except:
                    pass

            print(f"[IMAGES] {len(result)} Found")

            for item in result:

                print(item)

            return result

        except Exception as e:

            print(e)

            return []

    # ==========================================
    # TABLES
    # ==========================================

    @staticmethod
    def extract_tables():

        page = PageReader._page()

        try:

            tables = page.locator("table")

            result = []

            count = tables.count()

            for i in range(count):

                try:

                    text = tables.nth(i).inner_text()

                    result.append(text)

                except:
                    pass

            print(f"[TABLES] {len(result)} Found")

            return result

        except Exception as e:

            print(e)

            return []

    # ==========================================
    # LISTS
    # ==========================================

    @staticmethod
    def extract_lists():

        page = PageReader._page()

        try:

            lists = page.locator("ul,ol")

            result = []

            count = lists.count()

            for i in range(count):

                try:

                    text = lists.nth(i).inner_text()

                    result.append(text)

                except:
                    pass

            print(f"[LISTS] {len(result)} Found")

            return result

        except Exception as e:

            print(e)

            return []

    # ==========================================
    # PAGE INFO
    # ==========================================

    @staticmethod
    def page_info():

        page = PageReader._page()

        info = {

            "title": "",

            "url": "",

            "heading": ""

        }

        try:
            info["title"] = page.title()
        except:
            pass

        try:
            info["url"] = page.url
        except:
            pass

        try:
            info["heading"] = PageReader.read_heading()
        except:
            pass

        return info