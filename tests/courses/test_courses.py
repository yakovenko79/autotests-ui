import re

import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:

    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form_component.check_visible(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0'
        )

        create_course_page.create_course_exercises_toolbar_view_component.check_visible()

        create_course_page.check_visible_exercises_empty_view()
        create_course_page.create_course_exercises_toolbar_view_component.click_create_exercise_button()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form_component.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )

        create_course_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=False)
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            max_score='100',
            min_score='10',
            estimated_time='2 weeks'
        )

    @pytest.mark.test_edit_course
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form_component.check_visible(
            title="",
            estimated_time="",
            description="",
            min_score='0',
            max_score='0'
        )
        create_course_page.create_course_toolbar_view_component.create_course_button.check_disabled()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.create_course_form_component.fill(
            title='My Course',
            estimated_time='5 days',
            description='This is a course',
            min_score='10',
            max_score='100'
        )
        create_course_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=False)
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.check_current_url(re.compile('.*/#/courses'))
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            max_score='100',
            min_score='10',
            estimated_time='5 days',
            title='My Course'
        )
        courses_list_page.course_view.kebab.click_edit(index=0)
        create_course_page.check_current_url(re.compile(".*/#/courses/*."))
        create_course_page.create_course_toolbar_view_component.check_visible(
            "Update course",
            is_create_course_disabled=False)
        create_course_page.create_course_form_component.fill(
            title='Interesting Course',
            estimated_time='9.5 weeks',
            description='Course for adult',
            min_score='1',
            max_score='69'
        )
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.check_current_url(re.compile(".*/#/courses"))
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Interesting Course',
            estimated_time='9.5 weeks',
            min_score='1',
            max_score='69'
        )
