import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_first_test():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    browser.maximize_window()
    browser.get("https://ru.wikipedia.org/wiki/")
    browser.implicitly_wait(5)
    browser.find_element_by_name("search").send_keys("ГРАНДМАСТЕР")
    browser.close()

