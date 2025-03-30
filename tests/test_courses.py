from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

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

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_main_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_main_header).to_be_visible()
        expect(courses_main_header).to_have_text('Courses')

        results_header = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(results_header).to_be_visible()
        expect(results_header).to_have_text('There is no results')
