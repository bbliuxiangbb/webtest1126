#@Author: LIUXIANG
#@Time  :  2019/9/16 19:03

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
class TestCLFGLandYSZJjiekou(unittest.TestCase):
    '''职能端存量房系统，预售资金系统各查询，引用，调档功能测试'''
    # @classmethod  #类方法
    # def setUpClass(cls) -> None:
    #     cls.driver = webdriver.Firefox()
    #     loginxt(cls.driver, "lx022002", "lx022002")
        # self.login_page = LoginPage(self.driver)
    def setUp(self) -> None:
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        loginxt(self.driver, "lx022002", "lx022002")

    def tearDown(self) -> None:
        self.driver.close()

#存量房管理
    def testgg_01(self):
        '''存量房管理-窗口房源信息查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '40780f0b-9580-4392-a2c2-f547165f2683窗口房源信息']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_02(self):
        '''存量房管理-所有房源信息查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'f70a6a1a-e738-4ac1-b275-52a83dad895d所有房源信息']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_03(self):
        '''存量房管理-买卖合同管理查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'b087c133-940f-4aac-bdaa-22142eaf53a8买卖合同管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'zl_o_7']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_04(self):
        '''存量房管理-业务查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '752b54ce-8522-46ce-87e5-e0db86d10815业务查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_05(self):
        '''存量房管理-经纪服务合同查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '5299b05c-319b-42c0-a691-d2487c10dbbf经纪服务合同查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_06(self):
        '''存量房管理-江门-合同撤销申请查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'f660953d-b2ec-4c6b-a21c-1f1833aca620江门-合同撤销申请查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_07(self):
        '''存量房管理-江门—合同变更查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'cdbd6562-21d3-4cd9-9efa-e09e0d5c9dd1江门—合同变更查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_08(self):
        '''存量房管理-江门存量房买卖合同管理（职能端）查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'd84bd567-dc32-4cc2-8b09-b9fd2eafc0c6江门存量房买卖合同管理（职能端）']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_sel']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_09(self):
        '''存量房管理-待办业务查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '60f1dd36-33b1-4464-a0a2-c7f96ff1edd2待办业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_10(self):
        '''存量房管理-已办业务查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'f65d3b52-50cb-4aa0-b124-d1887b18106b已办业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_11(self):
        '''存量房管理-江门-合同撤销业务查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '15d3626a-a0bb-4342-a604-13953fd64c67江门-合同撤销业务查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_12(self):
        '''存量房管理-房源补录查询（职能端）查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '30db0ad2-2b72-4062-9fcf-c05158e0fac7房源补录查询（职能端）']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_13(self):
        '''存量房管理-合同备案,引用，保存功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '8edc32eb-e2b2-417a-b6d5-c2079d8af3d4合同备案']")
        dengdai(self.driver, loc2).click()   #点合同备案
        time.sleep(5)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc2 = ("xpath", "//*[@class = 'dhxtoolbar_text'and text()= '引用合同']")
        dengdai(self.driver, loc2).click()  # 点引用合同
        time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'/CLF/Compact/CiteContract?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc1 = ("xpath", "//*[@id= 'txt_search']")
        dengdai(self.driver, loc1).send_keys("JM ESM M2019000061")  # 输入合同
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loc0 = ("xpath", "//*[@name= 'checkRadio']")
        dengdai(self.driver, loc0).click()  # 点单选
        self.driver.switch_to.parent_frame()
        loc5 = ("xpath", "//*[@onclick = 'winModalDlg.getFrame().contentWindow.yyhtload(1);']")
        dengdai(self.driver, loc5).click()  # 点确定
        self.driver.switch_to.default_content()
        # t = self.driver.find_element_by_xpath("//*[text()= '确定']").text
        # print(t)
        loactor = (
            "xpath", "//*[text()= '确定']")  #
        element1 = WebDriverWait(self.driver, 100).until(
            EC.text_to_be_present_in_element(loactor, "确定"))
        assert element1  #

    def testgg_14(self):
        '''存量房管理-合同撤销,引用合同保存功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'cafffae5-1f20-4928-b52c-98d5d06c0fcb合同撤销']")
        dengdai(self.driver, loc2).click()  # 点合同撤销
        time.sleep(5)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc2 = ("xpath", "//*[@class = 'dhxtoolbar_text'and text()= '引用合同']")
        dengdai(self.driver, loc2).click()  # 点引用合同
        time.sleep(3)
        loactor = ("xpath", "//iframe[starts-with(@src,'/CLF/Compact/CiteContract?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc1 = ("xpath", "//*[@id= 'txt_search']")
        dengdai(self.driver, loc1).send_keys("JM ESM M2019000110")  # 输入合同
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loc0 = ("xpath", "//*[@name= 'checkRadio']")
        dengdai(self.driver, loc0).click()  # 点单选
        self.driver.switch_to.parent_frame()
        loc5 = ("xpath", "//*[@onclick = 'winModalDlg.getFrame().contentWindow.yyhtload(2);']")
        dengdai(self.driver, loc5).click()  # 点确定
        self.driver.switch_to.default_content()
        # t = self.driver.find_element_by_xpath("//*[text()= '确定']").text
        # print(t)
        loactor = (
            "xpath", "//*[text()= '确定']")  #
        element1 = WebDriverWait(self.driver, 100).until(
            EC.text_to_be_present_in_element(loactor, "确定"))
        assert element1  #
    def testgg_15(self):
        '''存量房管理-江门—合同变更,引用合同，保存功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='存量房管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'ed9f157e-7fcc-4af6-bdf5-453961a236c7合同变更']")
        dengdai(self.driver, loc2).click()  # 点江门—合同变更
        time.sleep(8)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc2 = ("xpath", "//*[@class = 'dhxtoolbar_text'and text()= '引用合同']")
        dengdai(self.driver, loc2).click()  # 点引用合同
        time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'/CLF/Compact/CiteContract?bid=')]")  # 切换iframe
        #loactor = ("xpath", "//iframe[starts-with(@src,'/CLF/Compact/jmCiteContract?bid=')]")  # 切换iframe江门合同变更
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc1 = ("xpath", "//*[@id= 'txt_search']")
        dengdai(self.driver, loc1).send_keys("JM ESM M2019000110")  # 输入合同
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loc0 = ("xpath", "//*[@name= 'checkRadio']")
        dengdai(self.driver, loc0).click()  # 点单选
        self.driver.switch_to.parent_frame()
        loc5 = ("xpath", "//*[@onclick = 'winModalDlg.getFrame().contentWindow.yyhtload(3);']")
        dengdai(self.driver, loc5).click()  # 点确定
        self.driver.switch_to.default_content()
        # t = self.driver.find_element_by_xpath("//*[text()= '确定']").text
        # print(t)
        loactor = ("xpath", "//*[text()= '确定']")  #
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "确定"))
        assert element1  #
#统计报表管理(江门)
    def testgg_16(self):
        '''统计报表管理(江门)-签约情况统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计报表管理(江门)']")
        dengdai(self.driver, loc1).click()
        # time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '0e166b53-aad7-47d4-84e0-bab4561b36cf签约情况统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_17(self):
        '''统计报表管理(江门)-成交情况统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计报表管理(江门)']")
        dengdai(self.driver, loc1).click()
        # time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '63c4718a-7bf6-40cc-a48b-0597a2a94718成交情况统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@id='gridbox_list']/div[1]/table/tbody/tr[2]/td[1]")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "合同来源"))
        assert element1  # 断言能不能获取 跳页

    def testgg_18(self):
        '''统计报表管理(江门)-中介签约情况统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='统计报表管理(江门)']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '32a23f29-3b97-4e7b-8343-3d4bf79fcb88中介签约情况统计']")
        dengdai(self.driver, loc2).click()  #dian ji中介签约情况统计
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        self.driver.switch_to.default_content()
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath",
            "//*[@style='float:left;width:34%;']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "技术支持：广州佳禾科技有限公司"))
        assert element1  # 断言能不能获取 跳页

    def testgg_19(self):
        '''统计报表管理(江门)-窗口成交情况统计查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='统计报表管理(江门)']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '7bc78c71-5cf7-4610-b7db-6320f7661633窗口成交情况统计']")
        dengdai(self.driver, loc2).click()#窗口成交情况统计
        time.sleep(1)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        self.driver.switch_to.default_content()
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = ("xpath", "//*[@style='float:left;width:34%;']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "技术支持：广州佳禾科技有限公司"))
        assert element1  # 断言能不能获取 跳页
#预售资金监管-
    def testgg_20(self):
        '''预售资金监管-缴款提醒查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'c684fa2b-31cc-44ca-a42c-38d47a51f339缴款提醒']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        self.driver.switch_to.default_content()
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath",
            "//*[@style='float:left;width:34%;']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(
            EC.text_to_be_present_in_element(loactor, "技术支持：广州佳禾科技有限公司"))
        assert element1  # 断言能不能获取 跳页

    def testgg_21(self):
        '''预售资金监管-按揭归集提醒查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'b11ae4bf-2f64-4b25-b694-53e030e48c02按揭归集提醒']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        self.driver.switch_to.default_content()
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath",
            "//*[@style='float:left;width:34%;']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(
            EC.text_to_be_present_in_element(loactor, "技术支持：广州佳禾科技有限公司"))
        assert element1  # 断言能不能获取 跳页

    def testgg_22(self):
        '''预售资金监管-缴款计划管理查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '10ee5c02-0310-47f3-a847-c6311a5929e0缴款计划管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_23(self):
        '''预售资金监管-资金入账管理查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'b3de1f1f-8f9c-4759-ae11-ab3367573849资金入账管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_24(self):
        '''预售资金监管-监管账户管理查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(2)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'f6ce283c-e09f-4272-a536-da08cf3ca45b监管账户管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_25(self):
        '''预售资金监管-资金划拨管理查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(2)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '3c9c0c27-6bf5-4e53-b2ae-4541af022c48资金划拨管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_26(self):
        '''预售资金监管-取消资金监管查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(2)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '9dd4a1ea-59d1-43d0-9467-16b1629f3b08取消资金监管']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_27(self):
        '''预售资金监管-对账管理查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(2)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '72bf422a-06a7-41b5-84ea-a71d3fae7f47对账管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_28(self):
        '''预售资金监管-楼盘管理查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(2)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '0b18ddef-e070-4d9b-8237-194a19f312c7楼盘管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_29(self):
        '''预售资金监管-资金归集查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '32f450de-6c5e-47f6-8669-ce4b1f0e4d2f资金归集查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_30(self):
        '''预售资金监管-银行对账查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'ce1b95fe-b95c-48bb-ab10-b0595fd24548银行对账查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_31(self):
        '''预售资金监管-监管任务分配管理查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '8d4e60ec-3540-422f-afb7-ddcb38b9a11d监管任务分配管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_32(self):
        '''预售资金监管-施工许可证申请查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '047016b9-18f3-48e7-b71a-947b388c8c37施工许可证申请查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_33(self):
        '''预售资金监管-监管账户管理-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'db05f3de-2055-470a-b4b9-16de62274e21监管账户管理-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_34(self):
        '''预售资金监管-资金划拨管理-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'df0e4d87-bff9-4b9d-a3d6-5c72ded26116资金划拨管理-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_35(self):
        '''预售资金监管-开发商监管信息申请管理-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '2dee474f-113a-4089-9ab0-401ff2cdd1a5开发商监管信息申请管理-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_36(self):
        '''预售资金监管-开发商监管资金比例设置-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '3da2aee6-eb9d-4e39-9190-cdec89a124c6开发商监管资金比例设置-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_37(self):
        '''预售资金监管-保函管理-清远查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'ba581ecc-08e3-46e8-a91d-34f6cff77642保函管理-清远']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'button']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_38(self):
        '''预售资金监管-监管账户管理-阳江查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'a9afbc9e-33a3-4d22-84a0-ae1f3f9ff950监管账户管理-阳江']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_39(self):
        '''预售资金监管-资金划拨管理-阳江查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'ddc04a48-7d71-4688-832e-52af3dc54214资金划拨管理-阳江']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_40(self):
        '''预售资金监管-监管账户管理-江门查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '453c88c5-c224-4b12-a8fb-15e8db750f2c监管账户管理-江门']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_41(self):
        '''预售资金监管-取消资金监管-江门查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '49cbd9f9-8d08-4c88-8317-7d099810eb5c取消资金监管-江门']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_42(self):
        '''预售资金监管-资金划拨管理-江门查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'ce912d38-e25a-4dd4-9535-cbe3e6ea2802资金划拨管理-江门']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_43(self):
        '''预售资金监管-对账管理-江门查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '7ee17c84-829d-476c-98fe-100454346511对账管理-江门']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_44(self):
        '''预售资金监管-对账管理-阳江查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '2ef0c2f2-f351-41d5-94b6-2ba6935e74ae对账管理-阳江']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_45(self):
        '''预售资金监管-预售合同网签情况统计表查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '7fdad0de-f796-4095-8c31-66f75432ff2a预售合同网签情况统计表']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@id='CYZHGL_list']/div[1]/table/tbody/tr[2]/td[3]")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "项目名称"))
        assert element1  # 断言能不能获取 跳页

    def testgg_46(self):
        '''预售资金监管-资金划拨管理—台山查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'd53f5b4a-4839-4adf-afab-d0aee9a5da7d资金划拨管理—台山']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_47(self):
        '''预售资金监管-资金入账管理-江门查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预售资金监管']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '113ebc7d-f6b7-4d5d-b5ae-e407d9fc8dfc资金入账管理-江门']")
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