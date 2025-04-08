import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'courses-list-toolbar-title-text', 'Title')
        self.add_course_button = Button(page, 'courses-list-toolbar-create-course-button', 'Button')

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Courses')

        self.add_course_button.check_visible()

    def click_add_course_button(self):
        self.add_course_button.click()
        self.check_current_url(re.compile('.*/#/courses/create'))
