""" Page object model for Home Page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_element import PageElement


class HomePage:
    """Page object model for Home Page."""

    def __init__(self, driver: WebDriver):
        """Default constructor.

        :param driver: WebDriver instance."""
        self.driver = driver
        self.search_button = PageElement(
            self.driver, (By.CSS_SELECTOR, "button.btn-default")
        )
        self.search_field = PageElement(self.driver, (By.NAME, "search"))
        self.shopping_cart = PageElement(
            self.driver, (By.CSS_SELECTOR, "button.btn-default")
        )
        self.shopping_cart_menu = PageElement(
            self.driver, (By.LINK_TEXT, "Shopping Cart")
        )

    def open(self) -> None:
        """Opens the home page."""
        self.driver.get("https://tutorialsninja.com/demo/index.php")

    def set_search_query(self, query: str) -> None:
        """Ввести ключевое слово (в шапке сайта)."""
        self.search_field.send_keys(query)

    def click_search(self) -> None:
        """Click the search button on the top."""
        self.search_field.click()

    def click_shopping_cart_button(self) -> None:
        """Click shopping cart button."""
        self.shopping_cart.click()

    def click_shopping_cart_menu(self) -> None:
        """Click shopping cart menu."""
        self.shopping_cart_menu.click()
