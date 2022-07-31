# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/24 16:00
# Tool ：IntelliJ IDEA
from time import sleep

import yaml
from selenium import webdriver


def get_cookie(driver):
    driver.get("https://work.weixin.qq.com")
    driver.find_element_by_xpath("//*[@id='indexTop']/div[2]/aside/a[1]").click()
    sleep(30)
    # 等待5秒，扫码登录
    cookies_data = driver.get_cookies()
    with open("data.yml", "w", encoding="utf-8") as f:
        yaml.dump(cookies_data, f)


def login(driver):
    driver.get("https://work.weixin.qq.com")
    with open("data.yml", 'r', encoding="utf-8") as f:
        cookies_data = yaml.safe_load(f)
        for cookie in cookies_data:
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    sleep(10)


class TestBusWechat:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # get_cookie(self.driver) # 首次登录或者cookie失效之后调用即可
        login(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_case1(self):
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']/span").click()
        n = 0
        while True:  # 参照 https://ceshiren.com/t/topic/12689/3
            try:
                n += 1
                self.driver.find_element_by_css_selector(".js_has_member .js_add_member").click()
                ele = self.driver.find_element_by_id("username")
                if ele:
                    break
            except:
                print(f"第{n}次没有找到元素")
        # 添加成员
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("邹旭")
        self.driver.find_element_by_xpath('//*[@id="memberAdd_english_name"]').send_keys("jaxb")
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys("zouxu13334")
        self.driver.find_element_by_xpath('//*[@id="memberAdd_biz_mail"]').send_keys("87855")
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys("13544553366")
        self.driver.find_element_by_xpath('//*[@id="memberAdd_mail"]').send_keys("214556@qq.com")
        self.driver.find_element_by_link_text("保存").click()
        sleep(10)

        # 校验
        username = self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[2]/td[2]').text
        department = self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[2]/td[4]').text
        phone = self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[2]/td[5]').text

        assert username == "邹旭"
        assert department == "hyb"
        assert phone == "13544553366"