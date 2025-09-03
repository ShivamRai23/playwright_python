# Import Playwright's sync API and pytest
from playwright.sync_api import Page, expect

# Example test case to check Google search
def test_google_search(page: Page):
    # Open Google
    page.goto("https://www.google.com")
    
    # Type into search box
    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    
    # Press Enter
    page.keyboard.press("Enter")
    
    # Assert that title contains "Playwright"
    expect(page).to_have_title(lambda title: "Playwright" in title)
