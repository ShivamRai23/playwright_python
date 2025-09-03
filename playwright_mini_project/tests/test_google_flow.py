############## Scenario Covered: #######################
#Open Website
#Verify Page Title
#Click a Button
#Fill Input Box
#Search and Validate
#Handle Popup/Alert
#Take Screenshot
#Simple Assertion
#Navigate Between Pages
#Close Browser

####################### Google Search Automation #####################  

# Sync version of the above test case

'''
import os
from playwright.sync_api import sync_playwright, expect

def test_google_search_flow():
    with sync_playwright() as p:
        # Launch Browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open Website (Google)
        page.goto("https://www.google.com")

        # Make sure screenshots folder exists
        os.makedirs("screenshots", exist_ok=True)

        # Save screenshot inside screenshots/ folder
        page.screenshot(path="screenshots/google_home.png")

        # Handle Cookies Popup (if appears)
        try:
            page.click("button:has-text('Accept all')")
            print("Cookies popup handled")
        except:
            print("No popup found")

        # Verify Page Title
        title = page.title()
        print("Page Title:", title)
        assert "Google" in title  # Simple assertion

        # Fill Input Box (Search query)
        page.get_by_role("combobox", name="Search").fill("Playwright Python")

        # Click a Button (Search button)
        page.keyboard.press("Enter")

        # Wait and Validate Search Results
        page.wait_for_selector("text=Playwright")
        assert "Playwright" in page.content()
        print("Search results validated ")

        # Take Screenshot
        page.screenshot(path="screenshots/google_home.png")
        print("Screenshot captured")

        # Navigate Between Pages
        page.goto("https://www.wikipedia.org")
        print("Navigated to:", page.title())
        page.go_back()  # Back to Google
        print("Went back to:", page.title())

        # Close Browser
        browser.close()
        '''

# async version of the above test case   

import asyncio
from playwright.async_api import async_playwright
import pytest

@pytest.mark.asyncio
async def test_google_search_flow():
    async with async_playwright() as p:
        # Launch Browser
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Open Website (Google)
        await page.goto("https://www.google.com")

        # Handle Cookies Popup (if appears)
        try:
            await page.click("button:has-text('Accept all')")
            print("Cookies popup handled")
        except:
            print("No popup found")

        # Verify Page Title
        title = await page.title()
        print("Page Title:", title)
        assert "Google" in title  # Simple assertion

        # Fill Input Box (Search query)
        await page.get_by_role("combobox", name="Search").fill("Playwright Python")

        # Click a Button (Search button)
        await page.keyboard.press("Enter")

        # Wait and Validate Search Results
        await page.wait_for_selector("text=Playwright")
        content = await page.content()
        assert "Playwright" in content
        print("Search results validated")

        # Take Screenshot
        await page.screenshot(path="screenshots/google_search.png")
        print("Screenshot captured")

        # Navigate Between Pages
        await page.goto("https://www.wikipedia.org")
        print("Navigated to:", await page.title())
        await page.go_back()  # Back to Google
        print("Went back to:", await page.title())

        # Close Browser
        await browser.close()

# Run the test
asyncio.run(test_google_search_flow())






