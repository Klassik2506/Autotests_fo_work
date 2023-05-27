import pytest
from selene import browser, have

@pytest.fixture(scope='function', autouse=True)
def init_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://b2b.rosbank-dom.ru')
    browser.element('#Username').type('lumenrulezzz@yandex.ru')
    browser.element('#passwordInput').type('Klassik123')
    browser.element('#submitButton').click()
    browser.element('#cur_user_name').should(have.exact_text('Данилов Николай'))
    yield
    browser.quit()
