#@Author: LIUXIANG
#@Time  :  2019/9/16 19:11

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from aip import AipOcr
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.login import loginxt
from common.login1 import loginxt1
from common.login2 import loginxt2
from common.login3 import loginxt3
from common.webwa import dengdai
from common.webwa import is_text_in_element
import os
import unittest
class TestYSZJTJFXjiekou(unittest.TestCase):
    '''职能端各预售资金统计分析，项目手册管理，楼盘表管理菜单查询，引用，调档功能测试'''
    # @classmethod  #类方法
    # def setUpClass(cls) -> None:
    #     cls.driver = webdriver.Firefox()
    #     loginxt(cls.driver, "lx022002", "lx022002")
        # self.login_page = LoginPage(self.driver)
    def setUp(self) -> None:
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        loginxt(self.driver, "lx022002", "lx022002")
    #
    def tearDown(self) -> None:
        self.driver.close()
# 统计分析（预售资金）
    def testgg_01(self):
        '''统计分析-监管账户汇总信息统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'e7b41186-1fb8-47ee-8aef-9864fbdc8d83监管账户汇总信息统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_02(self):
        '''统计分析-登记入账详细信息统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '2d65e1ad-15e5-4e81-95e1-0f7543db7628登记入账详细信息统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_03(self):
        '''统计分析-登记划拨详细信息统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '10641336-c392-491a-9640-755fe1d1f353登记划拨详细信息统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_04(self):
        '''统计分析-银行入账详细信息统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '67ae7582-c01e-42fa-ba67-b17ad3d16817银行入账详细信息统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_05(self):
        '''统计分析-银行划拨详细信息统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '8b6c8a22-5458-4ad3-a835-0ea08b7653d6银行划拨详细信息统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_06(self):
        '''统计分析-按揭归集汇总信息统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'd265d8f5-68e3-4711-944c-385bfa51ccd4按揭归集汇总信息统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_07(self):
        '''统计分析-按揭归集详细信息统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'b9de5fee-d70d-4eea-a505-f9fea3421e67按揭归集详细信息统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_08(self):
        '''统计分析-月度收支情况表统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '0819fd38-0856-4851-a2f8-5bc32f94823d月度收支情况表']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        time.sleep(2)
        js = '''document.getElementById("kssj").removeAttribute("readonly");
    
                               document.getElementById("kssj").value="2018-09-09"  '''
        self.driver.execute_script(js)
        time.sleep(1)
        jsa = '''document.getElementById("jssj").removeAttribute("readonly");
                             document.getElementById("jssj").value="2019-09-09"  '''
        time.sleep(1)
        self.driver.execute_script(jsa)
        # self.driver.find_element_by_xpath("//*[@id = 'jssj']").send_keys("2019-09-09")
        # js1 = '''document.getElementById("kssj").removeAttribute("readonly") ;
        #                 document.getElementById("kssj").value("2018-09-09")'''
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_09(self):
        '''统计分析-银行流水详细信息统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '12b5bfc4-ad51-43d6-bdb4-c96ef9f3b0e7银行流水详细信息统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_10(self):
        '''统计分析-中国银行监管账户统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '08640718-cc2c-442c-95e2-bee9300d71e8中国银行监管账户统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_11(self):
        '''统计分析-一般户异常流水统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'b8fd2782-927c-41c1-bc7e-7674c98ed11c一般户异常流水统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_12(self):
        '''统计分析-监管银行统计总表-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'e1be54c0-b46f-431b-96e6-c4df4f6592e1监管银行统计总表-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_13(self):
        '''统计分析-监管银行统计明细表-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '729e0e29-4891-4756-867b-7558c125ca5c监管银行统计明细表-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_14(self):
        '''统计分析-项目竣工情况统计表-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'ff224d0c-7526-4558-8786-29f175d88a5a项目竣工情况统计表-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@onclick= 'Btn_query_Fun();']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_15(self):
        '''统计分析-竣工验收统计表-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'a6da6c24-1345-47e2-a1a9-2e8127df8257竣工验收统计表-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@value = '查询']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_16(self):
        '''统计分析-监管账户汇总信息统计-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'e52565f9-41f3-4ebd-840c-43ee48479526监管账户汇总信息统计-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_17(self):
        '''统计分析-工作绩效统计表-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'd5092844-2e52-4c79-a6e0-07b96961ff7c工作绩效统计表-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_18(self):
        '''统计分析-预售账户收支信息-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '76043904-074e-404f-a01f-e7a89706a938预售账户收支信息-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@value = '查询']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_19(self):
        '''统计分析-登记划拨详细信息统计-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'de2d761c-a576-4e2d-bbe9-998de23a59ad登记划拨详细信息统计-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_20(self):
        '''统计分析-月度收支情况表-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '168d60c1-4b0e-4072-9d79-7072846178b9月度收支情况表-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_21(self):
        '''统计分析-登记划拨详细信息统计(江门)查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '435863d1-7b17-4870-99bd-2dd6cf1c3f10登记划拨详细信息统计(江门)']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_22(self):
        '''统计分析-施工许可统计明细表-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '5aa1957d-fe20-4cf8-9c9c-850c22a64983施工许可统计明细表-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_23(self):
        '''统计分析-预售账户进账统计报表-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '63e8a3ac-038e-4783-907e-c3ae3e1742f9预售账户进账统计报表-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_24(self):
        '''统计分析-施工账户进账统计报表-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计分析']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'a6afd408-0b8d-470e-b85f-148e1da456ae施工账户进账统计报表-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    # 预售资金-业务审核
    def testgg_25(self):
        '''预售资金-业务审核-已办结业务查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金-业务审核']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'fc58ae93-bdc2-4e17-8876-4612d55084ff已办结业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_26(self):
        '''预售资金-业务审核-待办业务查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金-业务审核']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '0dbc0a06-b55c-40ca-ba2f-54169926a5b3待办业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_27(self):
        '''预售资金-业务审核-已办业务查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金-业务审核']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '64073235-4897-4a4b-8805-e2317be116ea已办业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    # 预售款监管办件情况-清远
    def testgg_28(self):
        '''预售款监管办件情况-清远-待办件查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售款监管办件情况-清远']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'f00f0dcc-f0c1-4f49-a7cb-5c7d36122c0a待办件']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_29(self):
        '''预售款监管办件情况-清远-已办件查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售款监管办件情况-清远']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '2aca1443-6365-4ebd-b746-256f96d422ff已办件']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_30(self):
        '''预售款监管办件情况-清远-已办结查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售款监管办件情况-清远']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '312c79a6-fc4f-4895-8799-2876fd2818c9已办结']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    # 项目手册管理
    def testgg_31(self):
        '''项目手册管理-开发商监管信息管理-云浮查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='项目手册管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '183b0661-cac3-4d0d-9dd6-fb13106c8898开发商监管信息管理-云浮']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_sel']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_32(self):
        '''项目手册管理-项目建设预算管理查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='项目手册管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '4563bb25-d8a5-481c-8b1e-f724228c65fb项目建设预算管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_sel']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_33(self):
        '''项目手册管理-施工进度管理-云浮查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='项目手册管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'da84f6dc-cfc5-4211-83a2-f70e36507c87施工进度管理-云浮']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_sel']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_34(self):
        '''项目手册管理-项目融资管理查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='项目手册管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '0c4f3f4d-521b-41eb-af93-9f756ae0602f项目融资管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_sel']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_35(self):
        '''项目手册管理-项目资金使用管理查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='项目手册管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '3229ea5d-6100-49ff-b905-294af4d22863项目资金使用管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_sel']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


    def testgg_36(self):
        '''项目手册管理-工人工资银行对账查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='项目手册管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '514a035b-fdc3-49e5-9874-9e25c32e82ba工人工资银行对账查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_sel']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_37(self):
        '''项目手册管理-工人工资支付专户查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='项目手册管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'ff11b278-af67-408d-9d1e-8e7f10f1a78d工人工资支付专户查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_sel']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
##楼盘管理
    def testgg_38(self):
        '''楼盘管理-新建楼盘审核查询'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '7533942f-0ef8-4d36-b723-a85144e9fd85新建楼盘审核查询']")   #  30d7db50
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_39(self):
        '''楼盘管理-商品房添加'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'af9cd9c8-69e3-4c26-975a-6a20847d1e49商品房添加']")   #  3楼
        dengdai(self.driver, loc2).click()
        time.sleep(10)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btnYylp']")
        dengdai(self.driver, loc3).click()  # 点引用楼盘
        loactor = ("xpath", "//*[@id = 'iframelpxx']")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath","//*[@id = 'txt_search']")  # 30d7db50-3d0e-46f4-a803-dc84070a4f69
        dengdai(self.driver, loc3).send_keys("清远万达")
        loc4 = ("xpath","//*[@id = 'btn_search']")  # 30d7db50-3d0e-46f4-a803-dc84070a4f69新建楼盘审核查询
        dengdai(self.driver, loc4).click()
        loc5 = ("xpath", "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  #点公司
        dengdai(self.driver, loc5).click()
        loc6 = ("xpath",
                "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody"
                "/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  #点项目
        dengdai(self.driver, loc6).click()
        loc7 = ("xpath",
        "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody"
        "/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  #点自然幢
        dengdai(self.driver, loc7).click()
        loc8 = ("xpath", "//*[text()= '万达4']")  # 点逻辑幢
        time.sleep(5)
        dengdai(self.driver, loc8).click()
        loc9 = ("xpath", "//*[@id='gridbox_jgzhgl']/div[2]/table/tbody/tr[2]/td[1]/label/input")  # 选择房屋101
        dengdai(self.driver, loc9).click()
        loc10 = ("xpath","//*[text()= '保存']")  #
        dengdai(self.driver, loc10).click()
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_40(self):
        '''楼盘管理-商品房分割'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath",
                "//*[@id = '46667a08-a788-4d06-b524-31a619c2efed商品房分割']")  #
        dengdai(self.driver, loc2).click()
        time.sleep(10)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btnYylp']")
        dengdai(self.driver, loc3).click()  # 点引用楼盘
        loactor = ("xpath", "//*[@id = 'iframelpxx']")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'txt_search']")  # 30d7db50-3d0e-46f4-a803-dc84070a4f69
        dengdai(self.driver, loc3).send_keys("清远万达")
        loc4 = ("xpath", "//*[@id = 'btn_search']")  # 30d7db50-3d0e-46f4-a803-dc84070a4f69新建楼盘审核查询
        dengdai(self.driver, loc4).click()
        loc5 = ("xpath", "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  # 点公司
        dengdai(self.driver, loc5).click()
        loc6 = ("xpath",
         "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")
        dengdai(self.driver, loc6).click() # 点项目
        loc7 = ("xpath",
                "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody"
                "/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  # 点自然幢
        dengdai(self.driver, loc7).click()
        loc8 = ("xpath", "//*[text()= '万达4']")  # 点逻辑幢
        time.sleep(5)
        dengdai(self.driver, loc8).click()
        loc9 = ("xpath", "//*[@id='gridbox_jgzhgl']/div[2]/table/tbody/tr[2]/td[1]/label/input")  # 选择房屋101
        dengdai(self.driver, loc9).click()
        loc10 = ("xpath", "//*[text()= '保存']")  #
        dengdai(self.driver, loc10).click()
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_41(self):
        '''楼盘管理-商品房合并'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath",
                "//*[@id = '606dc510-bae5-4409-aa1c-2b8732e98a76商品房合并']")  # 3
        dengdai(self.driver, loc2).click()
        time.sleep(10)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btnYylp']")
        dengdai(self.driver, loc3).click()  # 点引用楼盘
        loactor = ("xpath", "//*[@id = 'iframelpxx']")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'txt_search']")  # 30d7db50-3d0e-46f4-a803-dc84070a4f69
        dengdai(self.driver, loc3).send_keys("清远万达")
        loc4 = ("xpath", "//*[@id = 'btn_search']")  # 30d7db50-3d0e-46f4-a803-dc84070a4f69新建楼盘审核查询
        dengdai(self.driver, loc4).click()
        loc5 = ("xpath", "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  # 点公司
        dengdai(self.driver, loc5).click()
        loc6 = ("xpath",
            "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")

        dengdai(self.driver, loc6).click()# 点项目
        loc7 = ("xpath",
                "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody"
                "/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  # 点自然幢
        dengdai(self.driver, loc7).click()
        loc8 = ("xpath", "//*[text()= '万达4']")  # 点逻辑幢
        time.sleep(5)
        dengdai(self.driver, loc8).click()
        loc9 = ("xpath", "//*[@id='gridbox_jgzhgl']/div[2]/table/tbody/tr[2]/td[1]/label/input")  # 选择房屋101
        dengdai(self.driver, loc9).click()
        loc0 = ("xpath", "//*[@id='gridbox_jgzhgl']/div[2]/table/tbody/tr[3]/td[1]/label/input")  # 选择房屋101
        dengdai(self.driver, loc0).click()
        loc10 = ("xpath", "//*[text()= '保存']")  #
        dengdai(self.driver, loc10).click()
        loactor = (
            "xpath", "//*[@id='btn_add']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "合并"))
        assert element1  # 断言能不能获取

    def testgg_42(self):
        '''楼盘管理-商品房修改'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath",
                "//*[@id = '04db8aa0-d8ce-4569-8015-25abd194cead商品房修改']")  # 30d7db50-3d0e-46f4-a803-dc84070a4f
        dengdai(self.driver, loc2).click()
        time.sleep(15)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btnYylp']")
        dengdai(self.driver, loc3).click()  # 点引用楼盘
        loactor = ("xpath", "//*[@id = 'iframelpxx']")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'txt_search']")  # 30d7db50-3d0e-46f4-a803-dc84070a4f69
        dengdai(self.driver, loc3).send_keys("清远万达")
        loc4 = ("xpath", "//*[@id = 'btn_search']")  # 30d7db50-3d0e-46f4-a803-dc84070a4f69新建楼盘审核查询
        dengdai(self.driver, loc4).click()
        loc5 = ("xpath", "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  # 点公司
        dengdai(self.driver, loc5).click()
        loc6 = ("xpath",
         "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")
        dengdai(self.driver, loc6).click()# 点项目
        loc7 = ("xpath",
                "//*[@id='model_treeBox']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody"
                "/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  # 点自然幢
        dengdai(self.driver, loc7).click()
        loc8 = ("xpath", "//*[text()= '万达4']")  # 点逻辑幢
        time.sleep(5)
        dengdai(self.driver, loc8).click()
        loc9 = ("xpath", "//*[@id='gridbox_jgzhgl']/div[2]/table/tbody/tr[2]/td[1]/label/input")  # 选择房屋101
        dengdai(self.driver, loc9).click()
        loc10 = ("xpath", "//*[text()= '保存']")  #
        dengdai(self.driver, loc10).click()
        self.driver.switch_to.default_content()
        loactor = (
            "xpath", "//*[@class='dhtmlx_popup_text']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 =(
        WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "当前引用的房屋已有在办业务")))
        assert element1  # 断言能不能获取

    def testgg_43(self):
        '''楼盘管理-商品房业务查询'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath",
                "//*[@id = 'b046db56-6471-4a30-8afc-2c81bdf7f54b商品房业务查询']")  #
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_44(self):
        '''楼盘管理-房屋分割'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'a2e3d47b-e6ed-47b1-a9b9-a53a81e547f2房屋分割']")  #
        dengdai(self.driver, loc2).click()
        time.sleep(10)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btnQuote']")
        dengdai(self.driver, loc3).click()  # 点引用楼盘
        time.sleep(3)
        # loactor = ("xpath", "//*[@id = 'iframelpxx']")  # 切换iframe
        # WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loactor = ("xpath", "//iframe[starts-with(@src,'/Spf/Lpb/lpbfwxx?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc0 = ("xpath", "//*[@id = 'CXFS']/option[2]")  # 选择等于条件
        dengdai(self.driver, loc0).click()
        loc3 = ("xpath", "//*[@id = 'CXNR']")  # 输入查询内容
        dengdai(self.driver, loc3).send_keys("44160200203118605199800895")
        loc4 = ("xpath", "//*[@id = 'queryBtn']")  # d点查询
        dengdai(self.driver, loc4).click()
        loc8 = ("xpath", "//*[@name = 'yyxxRadio']")  # \
        # time.sleep(5)
        dengdai(self.driver, loc8).click()
        self.driver.switch_to.parent_frame()
        loc9 = ("xpath", "//*[@onclick='winModalDlg.getFrame().contentWindow.submitLPBFWXX();']")  # 点保存
        dengdai(self.driver, loc9).click()
        self.driver.switch_to.default_content()
        loactor = (
            "xpath", "//*[@class='dhtmlx_popup_text']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = \
        WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "存在房屋已被调档，请重新选择"))
        assert element1  # 断言能不能获取

    def testgg_45(self):
        '''楼盘管理-房屋合并引用查询'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '84eb0a49-d3df-46ab-b192-9b8d43619493房屋合并']")  #
        dengdai(self.driver, loc2).click()
        time.sleep(15)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btnQuote']")
        dengdai(self.driver, loc3).click()  # 点引用楼盘
        time.sleep(3)
        # loactor = ("xpath", "//*[@id = 'iframelpxx']")  # 切换iframe
        # WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loactor = ("xpath", "//iframe[starts-with(@src,'/Spf/Lpb/hbfwyy?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc0 = ("xpath", "//*[@id = 'CXFS']/option[2]")  # 选择等于包含
        dengdai(self.driver, loc0).click()
        loc3 = ("xpath", "//*[@id = 'CXNR']")  # 输入查询内容
        dengdai(self.driver, loc3).send_keys("441602002031186051998007")
        loc4 = ("xpath", "//*[@id = 'queryBtn']")  # d点查询
        dengdai(self.driver, loc4).click()
        # loc8 = ("xpath", "//*[@name = 'yyxxRadio']")  # \
        # # time.sleep(5)
        # dengdai(self.driver, loc8).click()
        # self.driver.switch_to.parent_frame()
        # loc9 = ("xpath", "//*[@onclick='winModalDlg.getFrame().contentWindow.submitLPBFWXX();']")  # 点保存
        # dengdai(self.driver, loc9).click()
        self.driver.switch_to.default_content()
        loactor = (
            "xpath", "//*[@class='dhtmlx_popup_text']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(
            EC.text_to_be_present_in_element(loactor, "查无相关数据！"))
        assert element1  # 断言能不能获取

    def testgg_46(self):
        '''楼盘管理-楼盘表管理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '8d8712bb-0fe6-4730-ad81-7bc4ab292221楼盘表管理']")
        dengdai(self.driver, loc2).click()
        time.sleep(5)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 120).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        time.sleep(4)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id='selValue']")
        dengdai(self.driver, loc3).send_keys("河源万达广场有限公司1")  # 输入企业名称
        loc4 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc4).click()  # 点查询
        loc5 = ("xpath", "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]")
        dengdai(self.driver, loc5).click()
        loc6 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table"
                "/tbody/tr[1]/td[1]/div")
        dengdai(self.driver, loc6).click()
        loc1 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table"
                "/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")
        dengdai(self.driver, loc1).click()
        loc7 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[2]"
                "/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[4]/span")
        dengdai(self.driver, loc7).click()
        time.sleep(2)
        # time.sleep(20)
        # loactor =self.driver.find_element_by_xpath("//*[@id='text_list']/div[2]/table/tbody/tr[2]/td[4]").text
        # print(loactor)
        loactor = ("xpath", "//*[@id='text_list']/div[2]/table/tbody/tr[2]/td[4]")
        element1 = WebDriverWait(self.driver, 160).until(EC.text_to_be_present_in_element(loactor, ""))
        assert element1  # 断言能不能获取 文本为空

    def testgg_47(self):
        '''楼盘管理-房屋分割合并业务查询'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath",
                "//*[@id = '84989d34-58a3-4bd4-a9e3-64cfcdd3c634房屋分割合并业务查询']")  #
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@name = 'queryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_48(self):
        '''楼盘管理-楼盘锁定管理查询'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath",
                "//*[@id = '8b42b75e-03ec-48e1-b9ac-c85e1bd7a00d楼盘锁定管理']")  #
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_49(self):
        '''楼盘管理-楼盘表管理（全部房屋）菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='楼盘表管理1菜单']")
        # loc1 = ("xpath", "//*[text()='楼盘表管理']")   #'//*[text()='楼盘管理'
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '647c8a1d-306d-4d5e-a7c6-446f56e02742楼盘表管理（全部房屋）']")
        dengdai(self.driver, loc2).click()
        time.sleep(5)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 120).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        time.sleep(4)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id='selValue']")
        dengdai(self.driver, loc3).send_keys("河源万达广场有限公司1")  # 输入企业名称
        loc4 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc4).click()  # 点查询
        loc5 = ("xpath", "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]")
        dengdai(self.driver, loc5).click()
        loc6 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table"
                "/tbody/tr[1]/td[1]/div")
        dengdai(self.driver, loc6).click()#点项目
        loc1 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table"
                "/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")
        dengdai(self.driver, loc1).click()#点自然幢
        loc7 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[2]"
                "/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[4]/span")
        dengdai(self.driver, loc7).click()  #点逻辑幢
        time.sleep(2)
        # time.sleep(20)
        # loactor =self.driver.find_element_by_xpath("//*[@id='text_list']/div[2]/table/tbody/tr[2]/td[4]").text
        # print(loactor)
        loactor = ("xpath", "//*[@id='text_list']/div[2]/table/tbody/tr[2]/td[4]")
        element1 = WebDriverWait(self.driver, 160).until(EC.text_to_be_present_in_element(loactor, ""))
        assert element1  # 断言能不能获取 文本为空

















        # loc10 = ("xpath", "//*[text()= '保存']")  #
        # dengdai(self.driver, loc10).click()
        # loactor = (
        #     "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        # element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        # assert element1  # 断言能不能获取 跳页
        #








        # 'btn_search'
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        # loactor = (
        #     "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        # element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        # assert element1  #