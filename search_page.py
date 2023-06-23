from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class SearchPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self) -> None:
        self.driver.get("https://tutorialsninja.com/demo/index.php?route=product/search")

    def set_search_query(self, query: str) -> None:
        """Ввести ключевое слово (в шапке сайта)."""
        self.driver.find_element(By.NAME, "search").send_keys(query)

    def click_search(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()

    def set_search_criteria(self, query: str) -> None:
        """Ввести ключевое слово в Search Criteria."""
        self.driver.find_element(By.XPATH, "//input[@placeholder='Keywords']").send_keys(query)

    def click_search_criteria_button(self) -> None:
        """Клик на поиск под Search Criteria."""
        self.driver.find_element(By.ID, "button-search").click()