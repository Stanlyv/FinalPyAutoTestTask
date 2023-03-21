import time

import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize("url", [
    "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019']
                         )
def test_guest_can_add_product_to_basket(browser,url):
    page = ProductPage(browser, url)
    page.open()
    page.should_add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_notification()
    page.should_be_correct_basket_total()

@pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_find_broken_promo(browser,num):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, url)
    page.open()
    page.should_add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_notification()
    page.should_be_correct_basket_total()