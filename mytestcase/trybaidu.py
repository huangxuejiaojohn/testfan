from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from time import sleep
import HTMLTestRunner
import  unittest,re,time

class MyFirtUnit(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.baidu.com/"
        self.dr = webdriver.Firefox()
        self.verificationErrors = [] #若出现错误往verificationErrors中写入
        self.accept_next_alert = True

    def test_case_sousuo(self):
        self.dr.get(self.url)
        self.dr.find_element_by_id("kw").send_keys("selenium")
        sleep(3)

    def test_case_subiao(self):
        self.dr.get(self.url)
        hover  = self.dr.find_element_by_link_text("设置")
        ActionChains(self.dr).move_to_element(hover).perform()
        self.dr.find_element_by_link_text("搜索设置").click()
        sleep(3)
        self.dr.find_element_by_id("nr").find_element_by_xpath("//option[@value=20]").click()
        self.dr.find_element_by_link_text("保存设置").click()
        self.dr.switch_to.alert.accept()
        sleep(3)

    def tearDown(self):
        self.dr.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ =="__main__":
    unittest.main()