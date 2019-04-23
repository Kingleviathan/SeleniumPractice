from locators import Locators
from selenium import webdriver
import unittest


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_name = Locators.login_button_name

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(Locators.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(Locators.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_name(self.login_button_name).click()