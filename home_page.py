from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_element import PageElement


class HomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.search_button = PageElement(self.driver, (By.CSS_SELECTOR, "button.btn-default"))
        self.search_field = PageElement(self.driver, (By.NAME, "search"))
        self.shopping_cart = PageElement(self.driver, (By.CSS_SELECTOR, "button.btn-default"))
        self.shopping_cart_menu = PageElement(self.driver, (By.LINK_TEXT, "Shopping Cart"))

    def open(self) -> None:
        self.driver.get("https://tutorialsninja.com/demo/index.php")

    def set_search_query(self, query: str) -> None:
        """Ввести ключевое слово (в шапке сайта)."""
        self.search_field.send_keys(query)

    def click_search(self) -> None:
        self.search_field.click()

    def click_shopping_cart_button(self) -> None:
        self.shopping_cart.click()

    def click_shopping_cart_menu(self) -> None:
        self.shopping_cart_menu.click()
