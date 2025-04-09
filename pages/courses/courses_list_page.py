from playwright.sync_api import Page

from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavBarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_components import EmptyViewComponents
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.empty_view = EmptyViewComponents(page, 'courses-list')
        self.course_view = CourseViewComponent(page)
        self.navbar = NavBarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )
