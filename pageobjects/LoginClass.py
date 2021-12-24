from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    signi_account_box_ID = "nav-link-accountList"
    user_id_text_box_ID = "ap_email"
    continues_button_ID = "continue"
    password_text_box_ID = "ap_password"
    signin_submit_button_ID = "signInSubmit"

    def __init__(self, driver):
        self.driver = driver

    def click_sigin_account(self):
        self.driver.find_element(By.ID, self.signi_account_box_ID).click()

    def send_user_id(self, userid):
        self.driver.find_element(By.ID, self.user_id_text_box_ID).send_keys(userid)

    def click_continue(self):
        self.driver.find_element(By.ID, self.continues_button_ID).click()

    def send_password(self, password):
        self.driver.find_element(By.ID, self.password_text_box_ID).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(By.ID, self.signin_submit_button_ID).click()
