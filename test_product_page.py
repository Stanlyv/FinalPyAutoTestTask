import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page = LoginPage(browser, url)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, url)
        page.open()
        page.should_add_item_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_correct_notification()
        page.should_be_correct_basket_total()

    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
@pytest.mark.parametrize("url", [
    "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019']
                         )
def test_guest_can_add_product_to_basket(browser, url):
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

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.should_add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.should_add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_message()

def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear#"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.should_basket_is_empty()

@pytest.mark.xfail
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear#"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.should_basket_not_empty()













