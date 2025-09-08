from playwright.async_api import Page
from utils.helpers import screenshot_name

class SettingsPage:
    def __init__(self, page: Page):
        self.page = page

    async def open_settings(self):
        await self.page.get_by_role("link", name="Settings").click()
        await self.page.get_by_role("link", name="App Version").click()
        await self.page.get_by_role("link", name="Configuration").click()
        await self.page.get_by_role("link", name="Security").click()
        await self.page.get_by_role("link", name="Notifications").click()
        await self.page.get_by_role("link", name="Bulk Notifications").click()
        await self.page.get_by_role("link", name="List").click()
        await self.page.wait_for_timeout(1000)
        await self.page.screenshot(path=screenshot_name("settings"))

    async def logout(self):
        await self.page.get_by_role("link", name="Logout").click()
        await self.page.get_by_role("button", name="Yes, Take Action!").click()
        await self.page.wait_for_timeout(2000)
        await self.page.screenshot(path=screenshot_name("after_logout"))
