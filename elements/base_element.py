from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator) # self.page.locator(locator)

    def click(self, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.click()

    def check_visible(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)

def base():
    page = ...
    login_button = BaseElement(page, "test-login-button", "Login button")

    login_button.check_visible()
    login_button.click()


