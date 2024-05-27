from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.username = self.page.get_by_placeholder("Username")
        self.password = self.page.locator("[data-test=\"password\"]")
        self.login_button = self.page.locator("[data-test=\"login-button\"]")
        self.item = self.page.locator("[data-test=\"item-4-title-link\"]")
        self.add_to_cart = self.page.locator("[data-test=\"add-to-cart\"]")
        self.remove = self.page.locator("[data-test=\"remove\"]")
        self.open_menu = self.page.get_by_role("button", name="Open Menu")
        self.logout_button = self.page.locator("[data-test=\"logout-sidebar-link\"]")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login_logout(self):
        self.username.click()
        self.username.fill("standard_user")
        self.password.click()
        self.password.fill("secret_sauce")
        self.login_button.click()
        self.item.click()
        self.add_to_cart.click()
        self.remove.click()
        self.open_menu.click()
        self.logout_button.click()