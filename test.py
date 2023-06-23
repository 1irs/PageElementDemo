"""Basic tests for Open Cart."""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from home_page import HomePage
from search_page import SearchPage


def test() -> None:
    """Search for 'apple', look for MacBook."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    home_page = HomePage(driver)
    home_page.open()
    home_page.set_search_query("apple")
    home_page.open()

    assert "MacBook" in driver.page_source

    driver.quit()


def test_search_home() -> None:
    """Search for 'samsung' via header."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    home_page = HomePage(driver)
    home_page.open()
    home_page.set_search_query("samsung")
    home_page.click_search()

    assert "Search - samsung" in driver.page_source

    driver.quit()


def test_search_page() -> None:
    """Search for 'samsung' via search criteria button."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    search_page = SearchPage(driver)
    search_page.open()
    search_page.set_search_criteria("samsung")
    search_page.click_search_criteria_button()

    assert "Samsung SyncMaster 941BW" in driver.page_source

    driver.quit()
