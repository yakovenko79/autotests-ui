import pytest
from playwright.sync_api import sync_playwright, Page, Playwright, expect


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.firefox.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
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

    yield context

    context.close()
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state):
    page = initialize_browser_state.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    yield page
