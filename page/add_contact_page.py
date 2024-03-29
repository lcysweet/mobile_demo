import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddContactPage(BaseAction):

    # 姓名的输入框
    name_edit_text = By.XPATH, "//*[@text='姓名']"

    # 电话的输入框
    phone_edit_text = By.XPATH, "//*[@text='电话']"

    # 昵称输入框
    nickname_edit_text = By.XPATH,"//*[@text='昵称']"

    # 输入姓名
    @allure.step('输入姓名')
    def input_name(self, text):
        self.input(self.name_edit_text, text)

    # 输入电话
    @allure.step('输入电话')
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    # 输入昵称
    @allure.step('输入昵称')
    def input_nickname(self,text):
        self.input(self.nickname_edit_text,text)
