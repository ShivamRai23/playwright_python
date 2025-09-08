from playwright.async_api import Page
from utils.helpers import screenshot_name

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    async def goto_login_page(self):
        await self.page.goto("http://13.204.67.134:3001/admin/login")
        await self.page.screenshot(path=screenshot_name("login_page"))

    async def login(self, email: str, password: str):
        await self.page.get_by_role("textbox", name="Email").fill(email)
        await self.page.get_by_role("textbox", name="Password").fill(password)
        await self.page.get_by_role("button", name="Login").click()
        await self.page.wait_for_timeout(2000)
        await self.page.screenshot(path=screenshot_name("after_login"))
