import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0, "Number is less than zero"


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers_1(number: int, expected: int):
    assert number ** 2 == expected, f"Number {expected} is not equal to square {number}"


@pytest.mark.parametrize('os', ['Windows', 'MacOS', 'Linux', 'Debian'])
@pytest.mark.parametrize('browser', ['Chromium', 'Webkit', 'Firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=['Chromium', 'Webkit', 'Firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zare'])
class TestOperations:

    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'\nUser with operations: {user}')

    def test_user_without_operations(self, user: str):
        print(f'\nUser without operations: {user}')


users = {
    '+700000000001': 'user with money on bank account',
    '+700000000002': 'user without money on bank account',
    '+700000000003': 'user with operations on bank account',
    '+700000000004': 'user without operations on bank account'
}


@pytest.mark.parametrize('phone_number',
                         users.keys(),
                         ids=lambda phone_number: f'{phone_number}: {users[phone_number]}')
def test_identifiers(phone_number):
    ...
