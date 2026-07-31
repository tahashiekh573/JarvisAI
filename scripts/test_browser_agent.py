from app.browser.browser_agent import BrowserAgent

BrowserAgent.open("https://example.com")

BrowserAgent.title()

BrowserAgent.current_url()

BrowserAgent.extract_text("h1")

BrowserAgent.screenshot("example.png")

input("Press Enter...")

BrowserAgent.close()