# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/24 9:06
# Tool ：IntelliJ IDEA
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium_module.examples.base import Base


class TestBaidu(Base):
    def test_baidu_search(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("山上彻也" + Keys.SPACE + "刺杀安倍")
        self.driver.find_element(By.CSS_SELECTOR, "#su").click()
        sleep(3)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_baidu.py'])
