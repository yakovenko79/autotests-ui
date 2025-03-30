from playwright.sync_api import sync_playwright, expect

with sync_playwright() as phaywright:
    browser = phaywright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
        wait_until='networkidle'
    )

    new_text = 'New Text'
    page.evaluate(
        """
        (text) => {
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = text
    }
        """,
        new_text
    )

    page.wait_for_timeout(5000)