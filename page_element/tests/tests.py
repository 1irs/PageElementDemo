"""Test for PageElement."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_element.page_element import PageElement


def test_click(driver: WebDriver) -> None:
    """Test for the click method."""
    # 1. Открыть страницу с тестом.
    # 2. Найти элемент.
    # 3. Кликнуть по нему.
    # 4. Проверить, что клик прошел.
    button = PageElement(driver, (By.ID, "click"))
    span = PageElement(driver, (By.ID, "click_result"))
    button.click()

    assert span.text() == "Button clicked!"
