from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponents(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, '{identifier}-empty-view-icon', 'Empty view icon')
        self.title = Text(page, '{identifier}-empty-view-title-text', 'Empty view title')
        self.description = Text(page, '{identifier}-empty-view-description-text', 'Empty view description')

    def check_visible(self, identifier: str, title: str, description: str):
        self.icon.check_visible(identifier=identifier)
        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)
        self.description.check_visible(identifier=identifier)
        self.description.check_have_text(description, identifier=identifier)



