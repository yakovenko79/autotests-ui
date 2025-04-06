from re import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, '{identifier}-drawer-list-item-icon', 'Sidebar item icon')
        self.title = Text(page, '{identifier}-drawer-list-item-title-text', 'Sidebar item title')
        self.button = Button(page, '{identifier}-drawer-list-item-button', 'Sidebar item button')

    def check_visible(self, identifier: str, title: str):
        self.icon.check_visible(identifier=identifier)
        self.button.check_visible(identifier=identifier)
        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)
