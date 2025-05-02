import allure
import pytest
from playwright.sync_api import Page, Playwright
from _pytest.fixtures import SubRequest
from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page
from config import settings, Browser
from tools.routes import AppRoute


@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param)


@pytest.fixture(scope='session ')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form_component.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password)
    registration_page.click_registration_button()

    context.storage_state(path=settings.browser_state_file)

    browser.close()


@pytest.fixture(params=settings.browsers)
def page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name, 
        browser_type=request.param,
        storage_state=settings.browser_state_file
    )
