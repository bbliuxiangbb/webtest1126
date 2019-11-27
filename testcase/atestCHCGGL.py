#@Author: LIUXIANG
#@Time  :  2019/9/29 9:27

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
from common.base import Base
from common.webwa import is_text_in_element
import os
import unittest
class TestCLFGLandYSZJjiekou(unittest.TestCase):
    '''职能端测绘成果管理系统各查询，引用，调档功能测试'''
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

#测绘成果管理
    def testch_01(self):
        '''测绘成果管理-预测绘成果查询功能'''
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='测绘成果管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '77728ac2-7b6d-4334-be54-b23b52077b72预测绘成果查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testch_02(self):
        '''测绘成果管理-实测绘成果查询功能'''
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='测绘成果管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'e63671da-23a6-4738-a858-378e5aced097实测绘成果查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testch_03(self):
        '''测绘成果管理-预测绘成果管理查询功能'''
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='测绘成果管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '5d5267ce-437d-4518-b375-b53a393652ab预测绘成果管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testch_04(self):
        '''测绘成果管理-实测绘成果管理查询功能'''
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='测绘成果管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '0b6cc11a-387c-48de-a489-5579bd6b4a7d实测绘成果管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testch_05(self):
        '''测绘成果管理-预测绘成果业务查询-江门查询功能'''
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='测绘成果管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '27969dd0-a10e-4d33-afe8-1c2f64170a2b预测绘成果业务查询-江门']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testch_06(self):
        '''测绘成果管理-实测绘成果业务查询-江门查询功能'''
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='测绘成果管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'aaac30e0-a626-4b16-8cc8-91234b389886实测绘成果业务查询-江门']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testch_07(self):
        '''测绘成果管理-测绘成果管理待办业务查询功能'''
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='测绘成果管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'ca07c67c-262e-4083-b184-73ff9af6359c测绘成果管理待办业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testch_08(self):
        '''测绘成果管理-测绘成果管理已办业务查询功能'''
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='测绘成果管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '9cb45c5e-584c-4e1f-a181-72cd74583618测绘成果管理已办业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页