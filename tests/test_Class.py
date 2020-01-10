import pytest
from selenium import webdriver
from time import sleep


def test_first_test():
    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.maximize_window()
    browser.get("https://ru.wikipedia.org/wiki/")
    browser.implicitly_wait(5)
    browser.find_element_by_name("search").send_keys("ГРАНДМАСТЕР")
    browser.close()

