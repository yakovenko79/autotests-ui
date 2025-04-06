from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.navigation.navbar_component import NavBarComponent
from components.views.empty_view_components import EmptyViewComponents
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavBarComponent(page)
        self.create_course_form = CreateCourseExerciseFormComponent(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponents(page, 'create-course-exercises')

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_estimated_time_input = page.get_by_test_id(
            'create-course-form-estimated-time-input').locator('input')
        self.create_course_description_textarea = page.get_by_test_id('create-course-form-description-input').locator(
            'textarea').first

        self.create_course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        self.create_exercise_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_add_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise'
                                                              '-button')

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_disabled_create_course_button(self):
        expect(self.create_course_button).to_be_disabled()

    def check_visible_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str):
        expect(self.create_course_title_input).to_be_visible()
        expect(self.create_course_title_input).to_have_value(title)

        expect(self.create_course_estimated_time_input).to_be_visible()
        expect(self.create_course_estimated_time_input).to_have_value(estimated_time)

        expect(self.create_course_description_textarea).to_be_visible()
        expect(self.create_course_description_textarea).to_have_value(description)

        expect(self.create_course_max_score_input).to_be_visible()
        expect(self.create_course_max_score_input).to_have_value(max_score)

        expect(self.create_course_min_score_input).to_be_visible()
        expect(self.create_course_min_score_input).to_have_value(min_score)

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str):
        self.create_course_title_input.fill(title)
        self.create_course_estimated_time_input.fill(estimated_time)
        self.create_course_description_textarea.fill(description)
        self.create_course_max_score_input.fill(max_score)
        self.create_course_min_score_input.fill(min_score)

    def check_visible_exercises_title(self):
        expect(self.create_exercise_title).to_be_visible()
        expect(self.create_exercise_title).to_have_text('Exercises')

    def check_visible_create_exercise_button(self):
        expect(self.create_exercise_add_button).to_be_visible()
        expect(self.create_exercise_add_button).to_be_enabled()

    def click_create_exercise_button(self):
        self.create_exercise_add_button.click()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
