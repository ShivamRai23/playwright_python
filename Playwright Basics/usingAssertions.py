'''
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.wikipedia.org/")

    # Locate element using page.get_by_role (better than raw selectors)
    search_input = page.get_by_role("combobox", name="Search Wikipedia")

    # Type "Selenium"
    search_input.fill("Selenium")

    # Press Enter
    search_input.press("Enter")

    # Expect the page title to contain "Selenium"
    expect(page).to_have_title(lambda title: "Selenium" in title)

    browser.close()
'''


from playwright.sync_api import sync_playwright, expect
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.wikipedia.org/")

    # Locate element using page.get_by_role (better than raw selectors)
    search_input = page.get_by_role("combobox", name="Search Wikipedia")

    # Type "Selenium"
    search_input.fill("Selenium")

    # Press Enter
    search_input.press("Enter")

    # Expect the page title to contain