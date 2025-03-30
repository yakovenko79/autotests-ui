from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    courses_main_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_main_header).to_be_visible()
    expect(courses_main_header).to_have_text('Courses')

    chromium_page_with_state.wait_for_timeout(5000)

    results_header = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(results_header).to_be_visible()
    expect(results_header).to_have_text('There is no results')
