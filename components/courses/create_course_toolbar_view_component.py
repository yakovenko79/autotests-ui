import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Button')

    @allure.step("Check visible create course toolbar with title '{title}'")
    def check_visible(self, title='Create course', is_create_course_disabled=True):
        self.title.check_visible()
        self.title.check_have_text(title)
        self.create_course_button.check_visible()

        if is_create_course_disabled:
            self.create_course_button.check_disabled()

        if not is_create_course_disabled:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()
        self.check_current_url(re.compile(".*/#/courses"))
