import string

import pytest
from selene.support.shared import browser
from selene import be, have
import random


@pytest.fixture()
def generation_string():
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return random_string


def test_search_google_found(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in'))


def test_search_google_not_found(generation_string, open_browser):
    random_string = generation_string
    browser.element('[name="q"]').should(be.blank).type(random_string).press_enter()
    browser.element('.card-section').should(have.text(f'По запросу {random_string} ничего не найдено'))
