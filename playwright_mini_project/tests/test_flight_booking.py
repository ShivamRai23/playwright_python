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

###################### Flight Booking (Search Flight Flow) #######################

# Sync version of the above test case

''' 
from playwright.sync_api import sync_playwright

def test_search_flight_booking():
    with sync_playwright() as p:
        # Launch Browser
        browser = p.chromium.launch(headless=False, slow_mo=600)
        page = browser.new_page()

        # Open Flight Booking Demo Website
        page.goto("https://www.demoblaze.com/")  # Using DemoBlaze for demo purpose

        # Verify Page Title
        assert "STORE" in page.title()
        print("Title Verified: STORE")

        # Click a Button (Flights section - we simulate navigation)
        page.click("a:has-text('Laptops')")
        print("Clicked on Laptops section (simulating flights menu)")

        # Fill Input Box (Simulating search box)
        # Note: This site doesn’t have a search, so we simulate product filter
        page.click("a:has-text('Sony vaio i5')")
        print("Selected a product (as if searching flight)")

        # Simple Assertion
        assert "Sony" in page.content()
        print("Product details page verified")

        # Handle Popup/Alert (Add to cart triggers JS alert)
        page.click("a:has-text('Add to cart')")
        page.once("dialog", lambda dialog: dialog.accept())
        print("Handled alert: Product added to cart")

        # Take Screenshot
        page.screenshot(path="screenshots/flight_cart.png")
        print("Screenshot taken for cart page")

        # Navigate Between Pages
        page.go_back()   # Back to laptops list
        print("Navigated back to product list")
        page.go_forward()  # Forward to product page
        print("Navigated forward to product detail")

        # Close Browser
        browser.close()
        print("Browser Closed")
'''

# async version of the above test case   

import asyncio
from playwright.async_api import async_playwright
import pytest

@pytest.mark.asyncio
async def test_search_flight_booking():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=600)
        page = await browser.new_page()

        # Open Flight Booking Demo Website
        await page.goto("https://www.demoblaze.com/")  # Using DemoBlaze for demo purpose

        # Verify Page Title
        title = await page.title()
        assert "STORE" in title
        print("Title Verified: STORE")

        # Click a Button (Flights section - we simulate navigation)
        await page.click("a:has-text('Laptops')")
        print("Clicked on Laptops section (simulating flights menu)")

        # Fill Input Box (Simulating search box)
        await page.click("a:has-text('Sony vaio i5')")
        print("Selected a product (as if searching flight)")

        # Simple Assertion
        content = await page.content()
        assert "Sony" in content
        print("Product details page verified")

        # Handle Popup/Alert (Add to cart triggers JS alert)
        async def handle_dialog(dialog):
            await dialog.accept()
            print("Handled alert: Product added to cart")
        page.once("dialog", handle_dialog)
        await page.click("a:has-text('Add to cart')")

        # Take Screenshot
        await page.screenshot(path="screenshots/flight_cart.png")
        print("Screenshot taken for cart page")

        # Navigate Between Pages
        await page.go_back()
        print("Navigated back to product list")
        await page.go_forward()
        print("Navigated forward to product detail")

        # Close Browser
        await browser.close()
        print("Browser Closed")

# To run the async test directly
    asyncio.run(test_search_flight_booking())