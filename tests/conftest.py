import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.driver.set_window_size(1920, 1080)
    yield
    browser.quit()