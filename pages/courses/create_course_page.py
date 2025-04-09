from playwright.sync_api import Page

from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.navigation.navbar_component import NavBarComponent
from components.views.empty_view_components import EmptyViewComponents
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavBarComponent(page)
        self.create_course_form_component = CreateCourseFormComponent(page)
        self.create_course_toolbar_view_component = CreateCourseToolbarViewComponent(page)
        self.create_course_exercises_toolbar_view_component = CreateCourseExercisesToolbarViewComponent(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponents(page, 'create-course-exercises')

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
