import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, "logout")
        self.courses_list_item = SidebarListItemComponent(page, "courses")
        self.dashboard_list_item = SidebarListItemComponent(page, "dashboard")

    def check_visible(self):
        self.logout_list_item.check_visible(title='Logout')
        self.courses_list_item.check_visible(title='Courses')
        self.dashboard_list_item.check_visible(title='Dashboard')

    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r'.*/#/auth/login'))

    def click_course(self):
        self.courses_list_item.navigate(re.compile(r'.*/#/courses'))

    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r'.*/#/dashboard'))
