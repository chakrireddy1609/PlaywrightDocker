from Pages.LoginPage import LoginPage


def test_loginlogout(page):
    lp = LoginPage(page)
    lp.navigate()
    lp.login_logout()
