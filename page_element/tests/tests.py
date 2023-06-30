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


def test_text(driver: WebDriver) -> None:
    """Test for the text method."""
    assert (
        PageElement(driver, (By.ID, "test_text")).text()
        == "Where do you want to go today?"
    )


def test_send_keys(driver: WebDriver) -> None:
    """Test for the send_keys method."""
    input_el = PageElement(driver, (By.ID, "send_keys_input"))
    assert input_el.value() != "Hello, World!"

    input_el.send_keys("Hello, World!")
    assert input_el.value() == "Hello, World!"


def test_value(driver: WebDriver) -> None:
    """Test for the value method."""
    assert PageElement(driver, (By.ID, "test_value")).value() == "June, 30th"


def test_clear(driver: WebDriver) -> None:
    """TEst for the clear method."""
    test_clear_input = PageElement(driver, (By.ID, "test_clear"))
    assert test_clear_input.value() != ""

    test_clear_input.clear()
    assert test_clear_input.value() == ""
