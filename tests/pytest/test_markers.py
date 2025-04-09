import pytest


@pytest.mark.smoke
def test_smoke_case():
    pass


@pytest.mark.regression
def test_regression_case():
    pass


@pytest.mark.smoke
class TestSuite:

    @pytest.mark.regression
    def test_case1(self):
        ...

    def test_case2(self):
        ...


@pytest.mark.regression
class TestsUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass


@pytest.mark.critical
@pytest.mark.regression
@pytest.mark.smoke
def test_critical_login():
    ...


@pytest.mark.ui
class TestUserInterface:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass
