from app.browser.browser_manager import BrowserManager

page = BrowserManager.start()

page.goto("https://google.com")

input("Press Enter to close browser...")

BrowserManager.close()