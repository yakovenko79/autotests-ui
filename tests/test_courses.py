from playwright.sync_api import expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_main_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_main_header).to_be_visible()
    expect(courses_main_header).to_have_text('Courses')

    results_header = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(results_header).to_be_visible()
    expect(results_header).to_have_text('There is no results')
