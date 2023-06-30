"""Fixtures."""
import os
from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """Returns initialized WedDriver instance with a test page opened."""
    drv = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    abs_path = os.path.abspath("test.html")
    drv.get("file://" + abs_path)
    yield drv
    drv.quit()
