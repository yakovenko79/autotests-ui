from playwright.sync_api import sync_playwright, Page, expect
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_reg_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email_reg_input.fill('user@gmail.com')

    username_reg_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    username_reg_input.fill('username')

    password_reg_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    password_reg_input.fill('password')

    chromium_page.get_by_test_id('registration-page-registration-button').click()

    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()

#     context.storage_state(path='browser-state.json')
#
# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(storage_state='browser-state.json')
#     page = context.new_page()
#
#     page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
#
#     page.wait_for_timeout(500)
