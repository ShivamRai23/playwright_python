from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Step 1: Navigate to Google
        page.goto("https://www.google.com")

        # Step 2: Accept cookies popup (only appears in some regions)
        try:
            page.click("button:has-text('Accept all')")
        except:
            print("No cookies popup found")

        # Step 3: Fill the search box with "Playwright Python"
        search_box = page.locator("input[name='q']")
        search_box.fill("Playwright Python")

        # Step 4: Press Enter to search
        search_box.press("Enter")

        # Step 5: Wait for results page
        page.wait_for_selector("h3")
        print("✅ Search successful, results loaded!")

        browser.close()

