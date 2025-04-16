from playwright.sync_api import sync_playwright, Request, Response

from tools.routes import AppRoute


def log_request(request):
    print(f"Request: {request.url}")


def log_response(response):
    print(f"Response: {response.url}, {response.status}")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    page.on('request', log_request)
    page.on('response', log_response)

    page.wait_for_timeout(5000)
