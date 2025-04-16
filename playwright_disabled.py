from playwright.sync_api import sync_playwright, expect

from tools.routes import AppRoute

with sync_playwright() as phaywright:
    browser = phaywright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_disabled()

    page.wait_for_timeout(5000)