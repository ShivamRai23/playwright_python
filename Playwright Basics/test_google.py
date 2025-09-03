# Import sync_playwright from Playwright package
from playwright.sync_api import sync_playwright

# Entry point for running Playwright code in synchronous mode
with sync_playwright() as p:
    
    # Launch Chromium browser (set headless=False to actually see the browser window)
    browser = p.chromium.launch(headless=False)
    
    # Create a new browser tab (called 'Page' in Playwright)
    page = browser.new_page()
    
    # Go to Google's homepage
    page.goto("https://www.google.com")
    
    # Print confirmation in terminal
    print("✅ Google opened successfully")
    
    # Locate the search box by its 'name' attribute and type text into it
    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    
    # Press Enter to search
    page.keyboard.press("Enter")
    
    # Wait 3 seconds (just so you can see the result before browser closes)
    page.wait_for_timeout(3000)
    
    # Print the title of the page after search
    print("🔎 Page Title:", page.title())
    
    # Close the browser
    browser.close()


