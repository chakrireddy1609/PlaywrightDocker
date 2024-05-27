from playwright.sync_api import Page


class SortingProducts:
    def __init__(self, page:Page):
        self.page = page
        self.username = self.page.get_by_placeholder("Username")
        self.password = self.page.locator("[data-test=\"password\"]")
        self.login_button = self.page.locator("[data-test=\"login-button\"]")
        self.sort_dropdown = self.page.locator("[data-test=\"product-sort-container\"]")
        self.item5 = self.page.locator("[data-test=\"item-5-title-link\"]")
        self.back_to_products = self.page.locator("[data-test=\"back-to-products\"]")
        self.menu = self.page.get_by_role("button", name="Open Menu")
        self.logout_button = self.page.locator("[data-test=\"logout-sidebar-link\"]")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def sorting(self,username,password):
        self.username.click()
        self.username.fill(username)
        self.password.click()
        self.password.fill(password)
        self.login_button.click()
        self.sort_dropdown.click()
        self.item5.click()
        self.back_to_products.click()
        self.menu.click()
        self.logout_button.click()