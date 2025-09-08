from playwright.async_api import Page
from utils.helpers import screenshot_name

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate_dashboard(self):
        await self.page.locator("#layout-menu div").filter(has_text="Siren").get_by_role("link").nth(1).click()
        await self.page.get_by_role("link", name="Dashboard").click()
        await self.page.wait_for_timeout(1000)
        await self.page.screenshot(path=screenshot_name("dashboard"))

    async def open_subscriptions(self):
        await self.page.get_by_role("link", name="Subscriptions").click()
        await self.page.get_by_role("link", name="Subscription Plans").click()
        await self.page.get_by_role("link", name="Transaction History").click()
        await self.page.wait_for_timeout(1000)
        await self.page.screenshot(path=screenshot_name("subscriptions"))

    async def open_users(self, search_text: str):
        await self.page.get_by_role("link", name="Users").click()
        await self.page.get_by_role("textbox", name="Search...").fill(search_text)
        await self.page.locator("#userFilter").select_option("inactive")
        await self.page.locator("#userFilter").select_option("subscribed")
        await self.page.wait_for_timeout(1000)
        await self.page.screenshot(path=screenshot_name("users"))
