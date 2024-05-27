
def test_example(setup):
    page = setup
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"item-4-title-link\"]").click()
    page.locator("[data-test=\"add-to-cart\"]").click()
    page.locator("[data-test=\"remove\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()