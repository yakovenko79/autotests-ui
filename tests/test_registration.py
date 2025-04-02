from playwright.sync_api import sync_playwright, Page, expect
import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, username, password",
    [
        ("username@gmail.com", "username", "password")
    ]
)
def test_successful_registration(
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
        email: str,
        username: str,
        password: str
):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email, username, password)
    registration_page.click_registration_button()
    dashboard_page.should_be_current_url(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_page.check_dashboard_title()
