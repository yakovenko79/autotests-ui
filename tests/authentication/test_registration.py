import pytest
import allure
from allure_commons.types import Severity

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:

    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(
            self,
            registration_page: RegistrationPage,
            dashboard_page: DashboardPage,
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
    ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form_component.fill(email, username, password)
        registration_page.registration_form_component.check_visible(email, username, password)
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view_component.check_visible()
