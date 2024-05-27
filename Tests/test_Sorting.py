from Pages.SortingProducts import SortingProducts

def test_sorting(page):
    hp = SortingProducts(page)
    hp.navigate()
    hp.sorting("standard_user","secret_sauce")

