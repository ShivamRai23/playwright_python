import pytest
from playwright.async_api import async_playwright
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.settings_page import SettingsPage

@pytest.mark.asyncio
async def test_admin_flow():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context()
        page = await context.new_page()

        # Page objects
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)
        settings_page = SettingsPage(page)

        # Flow with screenshots
        await login_page.goto_login_page()
        await login_page.login("admin@gmail.com", "Admin@123")
        await dashboard_page.navigate_dashboard()
        await dashboard_page.open_subscriptions()
        await dashboard_page.open_users("sak")
        await settings_page.open_settings()
        await settings_page.logout()

        await context.close()
        await browser.close()
