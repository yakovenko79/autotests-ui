from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button


class CourseViewKebabComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.kebab_menu_button = Button(page, 'course-view-menu-button', "Kebab menu")
        self.edit_menu_button = Button(page, 'course-view-edit-menu-item', "Edit")
        self.delete_menu_button = Button(page, 'course-view-delete-menu-item', "Delete")

    def click_edit(self, index: int):
        self.kebab_menu_button.click(nth=index)

        self.edit_menu_button.check_visible(nth=index)
        self.edit_menu_button.click(nth=index)

    def click_delete(self, index: int):
        self.kebab_menu_button.click(nth=index)

        self.delete_menu_button.check_visible(nth=index)
        self.delete_menu_button.click(nth=index)
