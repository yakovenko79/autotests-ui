from playwright.sync_api import sync_playwright, expect

with sync_playwright() as phaywright:
    browser = phaywright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    for char in 'user.name@gmail.com':
        page.keyboard.type(char, delay=300)

    page.keyboard.press("ControlOrMeta+A")

    page.wait_for_timeout(5000)

