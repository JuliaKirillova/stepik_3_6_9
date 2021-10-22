import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# В коде реализован выбор языка для Chrome, так как это является достаточным для задания (см. п.5)

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                        help="Choose language: 'es' or 'fr'")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language == "fr":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif user_language == "es":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be 'es' or 'fr'")
    yield browser
    print("\nquit browser..")
    browser.quit()