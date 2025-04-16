from playwright.sync_api import sync_playwright, expect

from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)

    email_registration_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_registration_input.fill('user@gmail.com')

    username_registration_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_registration_input.fill('username')

    password_registration_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_registration_input.fill('password')

    page.get_by_test_id('registration-page-registration-button').click()

    context.storage_state(path='browser-state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, )
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto(AppRoute.COURSES)

    courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_header).to_be_visible()
    expect(courses_header).to_have_text('Courses')

    results_header = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(results_header).to_be_visible()
    expect(results_header).to_have_text('There is no results')
