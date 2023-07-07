"""Fixtures."""
import os
from typing import Generator
import pathlib

import pytest
from _pytest.fixtures import SubRequest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver() -> Generator[WebDriver, None, None]:
    """Returns initialized WedDriver instance with a test page opened."""

    # Set up.
    driver_kind = os.environ["DRIVER_KIND"]
    match driver_kind:
        case "chrome":
            drv: WebDriver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
            )
        case "remote":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--headless")
            drv = webdriver.Remote(
                command_executor="http://localhost:3000/webdriver",
                options=chrome_options,
            )
        case _:
            raise RuntimeError(
                f"Unknown DRIVER_KIND: {driver_kind}. Must be one of: chrome, remote."
            )

    yield drv

    # Tear down.
    drv.quit()


@pytest.fixture
def save_screenshot(
    driver: WebDriver, request: SubRequest
) -> Generator[None, None, None]:
    yield None
    driver.save_screenshot(f"reports/{request.node.name}.png")


@pytest.fixture
def page_under_test() -> str:
    """Gets address of a test page."""
    driver_kind = os.environ["DRIVER_KIND"]
    match driver_kind:
        case "chrome":
            abs_path = os.path.join(
                pathlib.Path(__file__).parent.resolve(), "test_files/test.html"
            )
        case "remote":
            abs_path = "/usr/src/app/workspace/test.html"
        case _:
            raise RuntimeError(
                f"Unknown DRIVER_KIND: {driver_kind}. Must be one of: chrome, remote."
            )

    return "file://" + abs_path
