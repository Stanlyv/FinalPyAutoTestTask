from selenium.common.exceptions import NoSuchElementException
url = ""

class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            print("\nНОУ САЧ ЕЛЕМЕНТ ЕКСЕПШН Ю НОУ")
            return False
        return True
