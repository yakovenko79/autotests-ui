import allure
from playwright.sync_api import Page, Locator, expect
from tools.logger import get_logger
from elements.ui_coverage import tracker
from ui_coverage_tool import ActionType, SelectorType

logger = get_logger("BASE_ELEMENT")


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self):
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with "data-testid={locator}" at the index "{nth}"'
        with allure.step(step):
            logger.info(step)
            return self.page.get_by_test_id(locator).nth(nth)  # self.page.locator(locator)

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        return f"//*[@data-testid='{self.locator.format(**kwargs)}'][{nth + 1}]"

    def track_coverage(self, action_type: ActionType, nth: int = 0, **kwargs):
        tracker.track_coverage(
            selector=self.get_raw_locator(nth, **kwargs),
            action_type=action_type,
            selector_type=SelectorType.XPATH
        )

    def click(self, nth: int = 0, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}" '
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.click()

        self.track_coverage(ActionType.CLICK, nth, **kwargs)

    def check_visible(self, nth: int = 0, **kwargs):
        step = f"Checking that {self.type_of} '{self.name}' is visible"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

        self.track_coverage(ActionType.VISIBLE, nth, **kwargs)

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        step = f"Checking that {self.type_of} '{self.name}' has text '{text}'"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)

        self.track_coverage(ActionType.TEXT, nth, **kwargs)


def base():
    page = ...
    login_button = BaseElement(page, "test-login-button", "Login button")

    login_button.check_visible()
    login_button.click()
