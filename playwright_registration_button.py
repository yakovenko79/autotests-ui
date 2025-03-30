from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    register_button = page.get_by_test_id('registration-page-registration-button')
    expect(register_button).to_be_disabled()

    email_register_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_register_input.fill('user.name@gmail.com')

    username_reg_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_reg_input.fill('username')

    password_reg_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_reg_input.fill('password')

    expect(register_button).to_be_enabled()
    register_button.click()
