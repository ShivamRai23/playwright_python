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

####################### Demo E-commerce (Login + Product Search) ######

# Sync version of the above test case

'''
from playwright.sync_api import sync_playwright

def test_ecommerce_flow():
    with sync_playwright() as p:
        # Launch Browser
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Open E-commerce Demo Website
        page.goto("https://www.saucedemo.com/")

        # Verify Page Title
        assert "Swag Labs" in page.title()
        print("itle Verified: Swag Labs")

        # Fill Input Box (Username & Password for login)
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")

        # Click Login Button
        page.click("input[type='submit']")

        # Simple Assertion (Check logged in by verifying URL)
        assert "inventory" in page.url
        print("Login Successful")

        # Search/Validate (Check product exists on homepage)
        page.wait_for_selector("text=Sauce Labs Backpack")
        assert page.is_visible("text=Sauce Labs Backpack")
        print("Product search validation done")

        # Handle Popup/Alert Simulation
        # (Here, we simulate adding to cart and alert check)
        page.click("button:has-text('Add to cart')")
        print("Product added to cart")

        # Take Screenshot of Cart Page
        page.click("a.shopping_cart_link")
        page.screenshot(path="cart_page.png")
        print("Screenshot taken for Cart Page")

        # Navigate Between Pages
        page.go_back()  # back to product page
        print("Went back to Product Page")
        page.go_forward()  # forward to cart page again
        print("Went forward to Cart Page")

        # Close Browser
        browser.close()
'''


# async version of the above test case  


import os
import asyncio
from playwright.async_api import async_playwright
import pytest

@pytest.mark.asyncio
async def test_ecommerce_product_flow():
    async with async_playwright() as p:
        # Launch Browser
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        page = await browser.new_page()

        # Open E-commerce Demo Website
        await page.goto("https://www.saucedemo.com/")

        # Make sure screenshots folder exists
        os.makedirs("screenshots", exist_ok=True)

        # Save screenshot inside screenshots/ folder
        await page.screenshot(path="screenshots/login_page.png")

        # Verify Page Title
        title = await page.title()
        assert "Swag Labs" in title
        print("Title Verified: Swag Labs")

        # Fill Input Box (Username & Password for login)
        await page.fill("input[name='user-name']", "standard_user")
        await page.fill("input[name='password']", "secret_sauce")

        # Click Login Button
        await page.click("input[type='submit']")

        # Simple Assertion (Check logged in by verifying URL)
        assert "inventory" in page.url
        print("Login Successful")

        # Search/Validate (Check product exists on homepage)
        await page.wait_for_selector("text=Sauce Labs Backpack")
        assert await page.is_visible("text=Sauce Labs Backpack")
        print("Product search validation done")

        # Handle Popup/Alert Simulation
        await page.click("button:has-text('Add to cart')")
        print("Product added to cart")

        # Take Screenshot of Cart Page
        await page.click("a.shopping_cart_link")
        await page.screenshot(path="screenshots/cart_page.png")
        print("Screenshot taken for Cart Page")

        # Navigate Between Pages
        await page.go_back()   # back to product page
        print("Went back to Product Page")
        await page.go_forward()  # forward to cart page again
        print("Went forward to Cart Page")

        # Close Browser
        await browser.close()


# Run the async test
asyncio.run(test_ecommerce_product_flow())


