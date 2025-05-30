from playwright.sync_api import sync_playwright, expect

from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill('password')

    page.get_by_test_id('login-page-login-button').click()

    page.wait_for_timeout(5000)

    alert = page.get_by_role("alert")

    text_alert = 'Wrong email or password'

    expect(alert).to_be_visible()
    expect(alert).to_have_text(text_alert)
