"""Fixtures."""
import os
from typing import Generator
import pathlib

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver() -> Generator[WebDriver, None, None]:
    """Returns initialized WedDriver instance with a test page opened."""

    # Set up.
    drv = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    abs_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "test.html")
    drv.get("file://" + abs_path)
    yield drv

    # Tear down.
    drv.quit()
