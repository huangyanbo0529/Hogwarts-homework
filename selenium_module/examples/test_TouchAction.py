# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/24 11:01
# Tool ：IntelliJ IDEA
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import TouchActions


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        """
        打开Chrome
        打开URL：https://www.baidu.com/
        向搜索框中输入'selenium测试'
        通过 TouchAction 点击搜索框
        滑动到底部，点击下一页
        关闭Chromr
        :return: None
        """
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.ID, "kw")
        ele_search = self.driver.find_element(By.ID, "su")
        ele.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        sleep(1)
        action.scroll_from_element(ele, 0, 10000)
        action.perform()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(5)
