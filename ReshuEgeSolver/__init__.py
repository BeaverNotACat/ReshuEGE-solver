import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from settings import *


class ReshuEgeSolver:
    def __init__(self):
        self.driver = eval("webdriver."+BROWSER+"()")

    def __log_in(self):
        self.driver.get("https://ege.sdamgia.ru")

        email_field = self.driver.find_element(By.ID, "email")
        email_field.send_keys(EMAIL)
        password_field = self.driver.find_element(By.ID, "current-password")
        password_field.send_keys(PASSWORD)
        password_field.submit()
        time.sleep(0.4)

    def __solve_test(self):
        self.driver.get(TEST_PAGE_URL)

        answer_forms = self.driver.find_elements(By.XPATH,
                                                 '//input[not(@type="hidden") and(contains(@class, "test_inp"))]')
        assert len(answer_forms) == len(TEST_ANSWERS), \
            "Answers and questions lenthes arent equal"

        for form in answer_forms:
            form.send_keys(TEST_ANSWERS.pop(0))

        self.driver.find_element(By.XPATH, '//input[contains(@onclick, "submit_form()")]').click()

    def run(self):
        self.__log_in()
        self.__solve_test()
        print('Requests completed')
