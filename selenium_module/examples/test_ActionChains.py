# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/24 10:19
# Tool ：IntelliJ IDEA
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    def test_case_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, "//input[@value='click me']")
        element_doubleclick = self.driver.find_element(By.XPATH, "//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)

    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.ID, "s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    def test_dragdrop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(By.ID, "dragger")
        drop_selement = self.driver.find_element(By.XPATH, "//div[@class='item'][4]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element, drop_selement).perform()
        # action.click_and_hold(drag_element).release(drop_selement).perform()
        action.click_and_hold(drag_element).move_to_element(drop_selement).release().perform()
        sleep(5)

    def test_keys(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH, "//*/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(2)
        action.send_keys(Keys.SPACE).pause(2)
        action.send_keys("tom").pause(2)
        action.send_keys(Keys.BACK_SPACE).send_keys(Keys.BACKSPACE).perform()
        sleep(5)
