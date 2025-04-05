from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('AddIcon')

        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')

        self.course_max_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')

        self.course_kebab_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_button = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_button = page.get_by_test_id('course-view-delete-menu-item')

        self.empty_new_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_new_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_new_description = page.get_by_test_id('course-min-score-info-row-view-text')

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        expect(self.empty_new_icon).to_be_visible()
        expect(self.empty_new_title).to_be_visible()
        expect(self.empty_new_title).to_have_text('There is no results')

        expect(self.empty_new_description).to_be_visible()
        expect(self.empty_new_description).to_have_text('Results from the load test pipeline will be displayed here')

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_visible_course_card(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str):
        expect(self.course_image.nth(index)).to_be_visible()

        expect(self.course_title.nth(index)).to_be_visible()
        expect(self.course_title.nth(index)).to_have_text(title)

        expect(self.course_max_text.nth(index)).to_be_visible()
        expect(self.course_max_text.nth(index)).to_have_text(f'Max score: {max_score}')

        expect(self.course_min_text.nth(index)).to_be_visible()
        expect(self.course_min_text.nth(index)).to_have_text(f'Min score: {min_score}')

        expect(self.estimated_time.nth(index)).to_be_visible()
        expect(self.estimated_time.nth(index)).to_have_text(f'Estimated time: {estimated_time}')

    def click_edit_course(self, index: int):
        self.course_kebab_menu_button.nth(index).click()
        expect(self.course_edit_menu_button.nth(index)).to_be_visible()
        self.course_edit_menu_button.click()

    def click_delete_course(self, index: int):
        self.course_kebab_menu_button.nth(index).click()
        expect(self.course_delete_menu_button.nth(index)).to_be_visible()
        self.course_delete_menu_button.click()
