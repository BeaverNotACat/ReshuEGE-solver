import time

import yaml
from yaml.loader import SafeLoader

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# from settings import *


class ReshuEgeSolver:
    settings = dict()

    def __init__(self, exam_url, answers_filename):
        with open("settings.yml", 'r') as stream:
            self.settings = yaml.load(stream, SafeLoader)
            print(self.settings)

        with open(answers_filename) as file:
            self.answers = [line.rstrip() for line in file]

        self.driver = eval("webdriver."+self.settings['BROWSER']+"()")
        self.exam_url = exam_url

    def __log_in(self):
        self.driver.get("https://ege.sdamgia.ru")

        email_field = self.driver.find_element(By.ID, "email")
        email_field.send_keys(self.settings['PROFILE']['EMAIL'])
        password_field = self.driver.find_element(By.ID, "current-password")
        password_field.send_keys(self.settings['PROFILE']['PASSWORD'])
        password_field.submit()
        time.sleep(0.4)

    def __solve_test(self):
        self.driver.get(self.exam_url)

        answer_forms = self.driver.find_elements(By.XPATH,
                                                 '//input[not(@type="hidden") and(contains(@class, "test_inp"))]')
        assert len(answer_forms) == len(self.answers), \
            "Answers and questions lenthes arent equal"

        for form in answer_forms:
            form.send_keys(self.answers.pop(0))

        self.driver.find_element(By.XPATH, '//input[contains(@onclick, "submit_form()")]').click()

    def run(self):
        self.__log_in()
        self.__solve_test()
        print('Requests completed')
