import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
        email="username@gmail.com",
        username="username",
        password="password"
):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form_component.fill(email, username, password)
    registration_page.registration_form_component.check_visible(email, username, password)
    registration_page.click_registration_button()
    dashboard_page.dashboard_toolbar_view_component.check_visible()
