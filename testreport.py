from selenium import webdriver
import HTMLTestRunner
import unittest


class MyFirstUnit(unittest.TestCase):
    mylst = [1, 2, 3]
    url = "http://www.baidu.com/"
    dr = webdriver.Firefox()
    def test_case_1(self):
        self.assertEqual("a", "a", "they are not equal.")  # assert 断言
        print("1111111111111111")

    def test_case_num(self):
        self.assertEqual("a", "a", "they are not equal.")  # assert 断言
        print("nnnnnn")

    def test_case_list(self):
        self.assertListEqual([1, 2, 3], self.mylst, "they are not equal.")
        print("LLLLLL")

    def test_case_baidu(self):
        self.dr.get(self.url)
        self.assertIn("百度一下",self.dr.title,"百度")

# def mysuite():
#     suite = unittest.TestSuite()
#     suite.addTest(MyFirstUnit("test_case_1"))
#     # suite.addTest(MyFirstUnit("test_case_list"))
#     suite.addTest(MyFirstUnit("test_case_num"))
#     suite.addTest(MyFirstUnit("test_case_baidu"))
#     return suite

if __name__ == "__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(MyFirstUnit("test_case_1"))
    testunit.addTest(MyFirstUnit("test_case_num"))
    testunit.addTest(MyFirstUnit("test_case_list"))
    testunit.addTest(MyFirstUnit("test_case_baidu"))
    filename = 'F:\\python脚本\\PycharmProjects\\untitled\\mygit\\testfan\\BaiduResult2.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='测试报告',
    description='用例执行情况：')
    runner.run(testunit)