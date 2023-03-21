from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_ITEM_NOTIFICATION = (By.XPATH, '//div[@id="messages"]')
    PRODUCT_NANE = (By.XPATH, '//div[contains(@class, "product_main")]//h1')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class, "product_main")]//p[@class="price_color"]')
    BASKET_TOTAL = (By.XPATH, '//div[contains(@class, "basket-mini")]')