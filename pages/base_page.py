from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until="networkidle")

    def reload(self):
        self.page.reload(wait_until="networkidle")

    def should_be_current_url(self, url: str):
        expect(self.page).to_have_url(url)
