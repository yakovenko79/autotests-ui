from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        page = browser.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill('password')

        page.get_by_test_id('login-page-login-button').click()

        alert = page.get_by_role("alert")

        expect(alert).to_be_visible()
        expect(alert).to_have_text('Wrong email or password')
