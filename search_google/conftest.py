import pytest
from selene.support.shared import browser


@pytest.fixture()
def set_window_size():
    browser.config.window_width = 1024
    browser.config.window_height = 768


@pytest.fixture()
def open_browser(set_window_size):
    browser.open('https://google.com')
    yield
    browser.quit()
