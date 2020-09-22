from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Insta_login:
    def __init__(self, username, pwd):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_class_name("f0n8F")\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pwd)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(1)  