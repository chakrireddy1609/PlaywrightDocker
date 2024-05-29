from Pages.LoginPage import LoginPage


def test_loginlogout(page):
    lp = LoginPage(page)
    lp.navigate()
    lp.login_logout()


def test_invalidlogin(page):
    lp1 = LoginPage(page)
    lp1.navigate()
    lp1.message_invalid_login()

def pagetitle(page):
    lp2 = LoginPage(page)
    lp2.navigate()
    lp2.assert_page_title()



