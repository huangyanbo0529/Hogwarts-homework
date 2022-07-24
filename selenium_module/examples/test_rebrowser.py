# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/24 15:47
# Tool ：IntelliJ IDEA
"""
【复用浏览器】
1.本地启动浏览器复用模式：cmd执行命令 chrome --remote-debugging-port=9222
2.启动浏览器输入网址：127.0.0.1:9222 或者 localhost:9222
"""

from selenium import webdriver


class TestReBrowser:
    def test_case(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
