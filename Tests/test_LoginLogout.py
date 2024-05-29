from Pages.LoginPage import LoginPage


def test_loginlogout(page):
    lp = LoginPage(page)
    lp.navigate()
    lp.login_logout()

def test_invalidLogin(page):
    lp1 = LoginPage(page)
    lp1.navigate()
    lp1.message_invalid_login()



