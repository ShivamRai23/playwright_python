import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("http://13.204.67.134:3001/admin/login")
    await page.get_by_role("textbox", name="Email").click()
    await page.get_by_role("textbox", name="Email").fill("admin@gmail.com")
    await page.get_by_role("textbox", name="Password").click()
    await page.get_by_role("textbox", name="Password").fill("Admin@11223")
    await page.locator("i").click()
    await page.get_by_role("textbox", name="Password").click()
    await page.get_by_role("textbox", name="Password").press("ArrowLeft")
    await page.get_by_role("textbox", name="Password").fill("Admin@1123")
    await page.get_by_role("textbox", name="Password").press("ArrowLeft")
    await page.get_by_role("textbox", name="Password").fill("Admin@123")
    await page.get_by_role("button", name="Login").click()
    await page.locator("#layout-menu div").filter(has_text="Siren").get_by_role("link").nth(1).click()
    await page.get_by_role("link", name="Dashboard").click()
    await page.get_by_role("link", name="Subscriptions").click()
    await page.get_by_role("link", name="Subscription Plans").click()
    await page.get_by_role("link", name="Transaction History").click()
    await page.get_by_role("link", name="Users").click()
    await page.get_by_role("textbox", name="Search...").click()
    await page.get_by_role("textbox", name="Search...").fill("sak")
    await page.locator("#userFilter").select_option("inactive")
    await page.locator("#userFilter").select_option("subscribed")
    await page.get_by_role("link", name="Settings").click()
    await page.get_by_role("link", name="App Version").click()
    await page.get_by_role("link", name="Configuration").click()
    await page.get_by_role("link", name="Security").click()
    await page.get_by_role("link", name="App Version").click()
    await page.get_by_role("link", name="Notifications").click()
    await page.get_by_role("link", name="Bulk Notifications").click()
    await page.get_by_role("link", name="List").click()
    await page.get_by_role("link", name="Logout").click()
    await page.get_by_role("button", name="Yes, Take Action!").click()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())