
from Pages.LoginPage import LoginPage
import pytest

def test_saucedemo(page):
    lp = LoginPage(page)
    lp.navigate()
    lp.login_logout()

