import allure
from playwright.sync_api import expect
from elements.base_element import BaseElement, logger


class Button(BaseElement):
    @property
    def type_of(self):
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        step = f"Checking that {self.type_of} '{self.name}' is enabled"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        step = f"Checking that {self.type_of} '{self.name}' is disabled"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()
