#@Author: LIUXIANG
#@Time  :  2019/8/28 14:13
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
class TestGGGLandCXBJjiekou(unittest.TestCase):
    '''职能端预售许可业务，商品房合同管理各菜单业务查询，引用，调档功能测试'''
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
    def testgg_01(self):
        '''公告管理，公告管理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(5)
        loc1 = ("xpath", "//*[text()='公告管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # time.sleep(3)
        # self.driver.find_element_by_xpath("//*[text()='公告管理']").click()
        loc2 = ("xpath", "//*[@id = '1318d068-196c-4af8-b6d9-939a30e1eeee公告管理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a=self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]") #切换iframe
        # self.driver.switch_to.frame(a)
        loc3= ("xpath","//*[@onclick= 'searchClick();']")
        dengdai(self.driver,loc3).click()  #点查询
        time.sleep(2)
        loactor = ("xpath","//*[@id='cxlb_pagingArea']/div/div[9]")
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  #断言能不能获取 首页
#诚信管理办件情况
    def testgg_02(self):
        '''诚信管理办件情况，待办业务菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='诚信管理办件情况']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '4e310d6e-6db2-4238-aac7-94c957243ba9待办业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_03(self):
        '''诚信管理办件情况，已办业务菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='诚信管理办件情况']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '4cbae48f-109e-416c-9c31-28d6e46a1068已办业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")   #"//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_04(self):
        '''诚信管理办件情况，已办结业务菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='诚信管理办件情况']")
        dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '538ca7b3-0011-4db2-9604-ae460e9df1b4已办结业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")   #"//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
#物业服务项目
    def testgg_05(self):
        '''物业服务项目---物业服务项目受理功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='物业服务项目']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '87b8c605-1522-497a-844a-c403f2bfdd68物业服务项目受理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(6)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor1 = ("xpath", "//*[@name = 'iframeslxx']")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor1))
        # time.sleep(3)
        # self.driver.switch_to.frame("iframeslxx")
        loc3 = ("xpath", "//*[@id= 'SQR']")
        dengdai(self.driver, loc3).send_keys("张枯") # 输入联系人
        loc4 = ("xpath", "//*[@class= 'dhxcombo_input']")
        dengdai(self.driver, loc4).click()  # 点击
        loc5 = ("xpath", "/html/body/div[2]/div[2]/div")
        dengdai(self.driver, loc5).click()  # 点击
        loc6 = ("xpath", "//*[@id= 'HTQXKSRQ']")
        dengdai(self.driver, loc6).send_keys("2019-08-28")  # 输入联系人
        loc7 = ("xpath", "//*[@id= 'HTQXJZRQ']")
        dengdai(self.driver, loc7).send_keys("2020-08-28")  # 输入联系人
        self.driver.switch_to.parent_frame()
        # self.driver.switch_to.default_content()
        loc8 = ("xpath", "//*[@id= 'btnSubmit']") #点提交
        dengdai(self.driver, loc8).click()
        time.sleep(3)
        self.driver.switch_to.default_content()
        loactor = ("xpath", "//*[@class = 'dhtmlx_popup_button']")
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "确定"))
        assert element1
    def testgg_06(self):
        '''物业服务项目---物业服务项目业务查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='物业服务项目']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'b8bf6044-347e-4a46-958c-0c863db61aa3物业服务项目业务查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_07(self):
        '''物业服务项目--物业服务项目查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='物业服务项目']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '2816b3e9-eb2c-4afe-aea0-994d3abf9387物业服务项目查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = ( "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
#物业服务企业诚信管理办件情况
    def testgg_08(self):
        '''物业服务企业诚信管理办件情况-待办业务查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='物业服务企业诚信管理办件情况']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'f58683fa-7bc0-4f81-8edf-f83e33417ecd待办业务']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
#xiugai and youhua daozheli
    def testgg_09(self):
        '''物业服务企业诚信管理办件情况-已办业务查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        loc1 = ("xpath", "//*[text()='物业服务企业诚信管理办件情况']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '86a19db6-1b6b-4297-92b8-de0117c42b8e已办业务']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        a = self.driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_10(self):
        '''物业服务企业诚信管理办件情况-已办结业务查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        loc1 = ("xpath", "//*[text()='物业服务企业诚信管理办件情况']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '3781113c-0554-457c-b703-134713821e26已办结业务']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(3)
        loactor = ( "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
#诚信管理综合待办业务
    def testgg_11(self):
        '''诚信管理综合待办业务-待办业务查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        loc1 = ("xpath", "//*[text()='综合待办业务']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '819ebaa6-8d7a-48fa-a140-60395966d5e8待办业务']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(3)
        loactor = (
        "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
#开发项目管理
    def testgg_12(self):
        '''开发项目管理-项目备案查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        loc1 = ("xpath", "//*[text()='开发项目管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'f1f7b860-bda9-4662-9438-b15cf6b15b84项目备案查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(3)
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_13(self):
        '''开发项目管理-开发项目查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        loc1 = ("xpath", "//*[text()='开发项目管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'e7390048-1332-4957-b78d-cfe852b8fb57开发项目查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(8)
        a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id='Btn_Seach']")      #"//*[@id= 'btn_search']"
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(3)
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_14(self):
        '''开发项目管理-项目进度管理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='开发项目管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'c9928170-178a-4f62-9d67-92e842ddb663项目进度管理']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        a = self.driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(3)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = ("xpath", "//*[@class ='dataTable_TY btn btn-small btn-primary']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        # print(loactor)
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, ""))
        assert element1  # 断言能不能获取 跳页
#预(销)售管理
    def testgg_15(self):
        '''预（销）售许可管理-房地产开发投资和市场运行情况调查表查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'ad3d0e61-d839-4d37-beb4-d8fb6e786b2a房地产开发投资和市场运行情况调查表查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(3)
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_16(self):
        '''预(销)售管理-企业申请查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(3)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '6abf741a-1c8a-4fec-befa-067d6f156a97企业申请查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(15)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 300).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id= 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 300).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_17(self):
        '''预(销)售管理-预（销）售许可管理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'da535077-1900-4b1a-afb1-b23978a72412预（销）售许可管理']")
        dengdai(self.driver, loc2).click()
        time.sleep(6)
        # loactor = ("xpath","//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # a = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id= 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = (
        "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_18(self):
        '''预(销)售管理-合同模板管理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '66cefa98-b702-40f1-96d1-a6e005cfbfcf合同模板管理']")
        dengdai(self.driver, loc2).click()
        time.sleep(5)
        loactor = ("xpath","//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 180).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 180).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_19(self):
        '''预(销)售管理-楼盘表管理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '8a2a0592-ec91-42f2-9547-281aef35751e楼盘表管理']")
        dengdai(self.driver, loc2).click()
        time.sleep(5)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 120).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        time.sleep(4)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id='selValue']")
        dengdai(self.driver, loc3).send_keys("万达") # 输入企业名称
        loc4 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc4).click()  #  点查询
        loc5 = ("xpath", "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]")
        dengdai(self.driver, loc5).click()
        loc6 = ("xpath", "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[1]/div")
        dengdai(self.driver, loc6).click()
        loc1 = ("xpath","//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")
        dengdai(self.driver, loc1).click()
        loc7 = ("xpath", "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[4]/span")
        dengdai(self.driver, loc7).click()
        time.sleep(2)
        # time.sleep(20)
        # loactor =self.driver.find_element_by_xpath("//*[@id='text_list']/div[2]/table/tbody/tr[2]/td[4]").text
        # print(loactor)
        loactor = ("xpath","//*[@id='text_list']/div[2]/table/tbody/tr[2]/td[4]")
        element1 = WebDriverWait(self.driver, 160).until(EC.text_to_be_present_in_element(loactor, ""))
        assert element1  # 断言能不能获取 文本为空

    def testgg_20(self):
        '''预(销)售管理-业务查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'b3394140-232d-4dea-9cf9-7ef5be26dc9e业务查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(8)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 300).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = (
        "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 180).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_21(self):
        '''预(销)售管理-楼盘表查看菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(1)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '643c2492-3928-4d3f-9a57-753774f8ea7c楼盘表查看']")
        dengdai(self.driver, loc2).click() #点楼盘表查看
        time.sleep(5)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 300).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id='selValue']")
        dengdai(self.driver, loc3).send_keys("万达")  # 输入企业名称
        loc4 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc4).click()  # 点查询
        loc5 = ("xpath", "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]")
        dengdai(self.driver, loc5).click()
        loc6 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[1]/div")
        dengdai(self.driver, loc6).click()
        loc1 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")
        dengdai(self.driver, loc1).click()
        loc7 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[4]/span")
        dengdai(self.driver, loc7).click()
        time.sleep(2)
        # time.sleep(20)
        # loactor =self.driver.find_element_by_xpath("//*[@id='text_list']/div[2]/table/tbody/tr[2]/td[4]").text
        # print(loactor)
        loactor = ("xpath", "//*[@id='text_list']/div[2]/table/tbody/tr[2]/td[4]")
        element1 = WebDriverWait(self.driver, 300).until(EC.text_to_be_present_in_element(loactor, ""))
        assert element1  # 断言能不能获取 文本为空
        # self.assertTrue(loactor = element1)
    def testgg_22(self):
        '''预(销)售管理-房地产市场指标上报查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'e560e710-b2a2-4a6e-8f9c-9a51cb99cb36房地产市场指标上报查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(8)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
#####
    def testgg_23(self):
        '''预(销)售管理-房地产市场指标统计报表菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
        self.driver.execute_script(js)
        time.sleep(1)
        js1 = 'document.getElementById("a197775d-be27-4d28-8003-b159499a8f61房地产市场指标统计报表").click()'
        time.sleep(1)
        self.driver.execute_script(js1)
        time.sleep(1)
        # loc2 = ("xpath", "//*[@id = 'a197775d-be27-4d28-8003-b159499a8f61房地产市场指标统计报表']")
        # dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
####
    def testgg_24(self):
        '''预(销)售管理-商品房价格备案查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
        self.driver.execute_script(js)
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'c3c0c03c-e118-41ba-8b84-14da78254429商品房价格备案查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    #
    #
    def testgg_25(self):
        '''预(销)售管理-待办业务查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(3)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
        self.driver.execute_script(js)
        time.sleep(3)
        # loc2 = ("xpath", "44069274-0515-4551-a7d1-2eb81754fb4e待办业务']")
        # dengdai(self.driver, loc2).click()
        js1 = 'document.getElementById("44069274-0515-4551-a7d1-2eb81754fb4e待办业务").click()'
        time.sleep(1)
        self.driver.execute_script(js1)
        time.sleep(7)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_26(self):
        '''预(销)售管理-已办业务查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(3)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
        self.driver.execute_script(js)
        time.sleep(3)
        # loc2 = ("xpath", "44069274-0515-4551-a7d1-2eb81754fb4e待办业务']")
        # dengdai(self.driver, loc2).click()
        js1 = 'document.getElementById("80163a04-e1f7-401f-85bf-edb292c757d6已办业务").click()'
        time.sleep(1)
        self.driver.execute_script(js1)
        time.sleep(5)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页





    # def testgg_27(self):
    #     '''预(销)售管理-楼盘房屋信息统计查询菜单查询功能'''
    #     # self.driver = webdriver.Firefox()
    #     # loginxt(self.driver, "lx022002", "lx022002")
    #     time.sleep(3)
    #     loc1 = ("xpath", "//*[text()='预(销)售管理']")
    #     dengdai(self.driver, loc1).click()
    #     time.sleep(3)
    #     js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
    #     self.driver.execute_script(js)
    #     time.sleep(3)
    #     # loc2 = ("xpath", "44069274-0515-4551-a7d1-2eb81754fb4e待办业务']")
    #     # dengdai(self.driver, loc2).click()
    #     js1 = 'document.getElementById("c3c9d39b-2958-4850-bc5c-d9eb4ce068fa楼盘房屋信息统计查询").click()'
    #     time.sleep(1)
    #     self.driver.execute_script(js1)
    #     time.sleep(5)
    #     loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
    #     WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
    #     # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
    #     # self.driver.switch_to.frame(a)
    #     js2 = 'document.getElementsByClassName("dhxcombo_input")[0].value="江门天地有限公司" '
    #     time.sleep(1)
    #     self.driver.execute_script(js2)
    #     time.sleep(1)
    #     js3 = 'document.getElementsByClassName("dhxcombo_input")[1].value="三三" '
    #     time.sleep(1)
    #     self.driver.execute_script(js3)
    #     time.sleep(1)
    #     # js4 = 'document.getElementsByClassName("dhxcombo_select_img")[2].click()'
    #     # time.sleep(1)
    #     # self.driver.execute_script(js4)
    #     # time.sleep(1)
    #     # js5 = 'document.getElementsByClassName("dhxcombo_checkbox dhxcombo_chbx_1")[0].click() '
    #     # time.sleep(1)
    #     # self.driver.execute_script(js5)
    #     # time.sleep(1)
    #
    #     # loc1 = ("xpath", "//*[@id='zrzlb']/div/div[1]/div")   #dhxcombo_cell_text
    #     # dengdai(self.driver, loc1).click()  # 点查询
    #     # loc2 = ("xpath", "//*[@class='dhxcombo_checkbox dhxcombo_chbx_1']")
    #     # dengdai(self.driver, loc2).click()  # 点查询
    #     # loc3 = ("xpath", "//*[@id= 'cxan']")
    #     # dengdai(self.driver, loc3).click()  # 点查询
    #
    #     js6 = 'document.getElementsById("cxan").click()'
    #     time.sleep(1)
    #     self.driver.execute_script(js6)
    #     time.sleep(1)
        # loactor = (
        #     "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        # element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        # assert element1  # 断言能不能获取 跳页
        #
        #
        # loactor = (
        # "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        # element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        # assert element1  # 断言能不能获取 跳页
    def testgg_27(self):
        '''预(销)售管理-装修标准菜单新增查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'ae4d32b9-78b4-42fc-91d0-1fa686873131装修标准']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class = 'add']")
        dengdai(self.driver, loc3).click()  # 点新增
        loc4 = ("xpath", "//*[@name= 'ZXBZSM']")
        dengdai(self.driver, loc4).send_keys("203289893")  #说明
        time.sleep(3)   #//*[@class = 'dhxform_btn_txt' and text()= '保存']
        loc5 = ("xpath", "//*[@id='myForm']/div/div[3]/div/div/div/div[7]/div/div/div[1]/div/div/div[2]")  #
        dengdai(self.driver, loc5).click() # 点保存
        # loactor = (
        #     "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        # element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        # assert element1  # 断言能不能获取 跳页
    def testgg_28(self):
        '''预(销)售管理-项目进度管理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '93ce1177-1af2-4f58-aab2-d20af9221520项目进度管理']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id = 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_29(self):
        '''预(销)售管理-项目进度管理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '3a139811-856e-4f15-8f64-766d52a4df12合同模板变更查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(5)
        a = self.driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_30(self):
        '''预(销)售管理-房地产开发投资和市场运行情况调查表查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'ad3d0e61-d839-4d37-beb4-d8fb6e786b2a房地产开发投资和市场运行情况调查表查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        a = self.driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_31(self):
        '''预(销)售管理-合同模板变更受理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '9cacf0c7-c6fb-4f00-8d9b-84fd73196f23合同模板变更受理']")
        dengdai(self.driver, loc2).click()
        time.sleep(15)
        a = self.driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnCiteContract']")
        dengdai(self.driver, loc3).click()  # 点引用模板按钮
        loactor = ("xpath", "//iframe[starts-with(@src,'/spf/Htmbbg/htmbbgsqYymb?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询i
        time.sleep(12)
        loc3 = ("xpath", "//*[@name= 'checkRadio']")
        dengdai(self.driver, loc3).click()  # 点选择单选
        time.sleep(1)
        self.driver.switch_to.parent_frame()
        loc4 = ("xpath","//*[@onclick = 'winModalDlg.getFrame().contentWindow.loadlist();']")
        dengdai(self.driver, loc4).click()  #点确定
        time.sleep(20)
        loc5 = ("xpath", "//*[@id= 'BZ']")
        dengdai(self.driver, loc5).send_keys("20190830HTMBBG")  # 输入变更原因
        loc6 = ("xpath", "//*[@id= 'btnSubmit']")
        dengdai(self.driver, loc6).click()  # 点提交按钮
        time.sleep(10)
        loactor = ("xpath", "//iframe[starts-with(@src,'/SPF/Txyj/Txyj?ywid=')]")  # 切换iframe
        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc5 = ("xpath", "//*[@id= 'txtspyj']")
        dengdai(self.driver, loc5).send_keys("20190830审核通过")  # 输入意见
        self.driver.switch_to.default_content()
        a = self.driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc4 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.SubmitTxyj();']")
        dengdai(self.driver, loc4).click()  # 点确定
        time.sleep(25)
        self.driver.switch_to.default_content()
        # self.driver.find_element_by_xpath("//*[text()= '确定']")
        # time.sleep(40)
        # t = self.driver.find_element_by_xpath("//*[text()= '确定']").text
        # print(t)
        # assert  t
        loactor = (
            "xpath", "//*[text()= '确定']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "确定"))
        assert  element1

    def testgg_32(self):
        '''预(销)售管理-楼盘表管理（商品房）查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='预(销)售管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '26681191-5323-46f0-bcc1-8791fbf4715d楼盘表管理（商品房）']")
        dengdai(self.driver, loc2).click()
        time.sleep(1)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id='selValue']")
        dengdai(self.driver, loc3).send_keys("江门天地有限公司")  # 输入企业名称
        loc4 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc4).click()  # 点查询
        time.sleep(2)
        loc5 = ("xpath", "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  #点公司
        dengdai(self.driver, loc5).click()
        loc6 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  #点项目
        dengdai(self.driver, loc6).click()
        loc1 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div")  ##d点自然幢
        dengdai(self.driver, loc1).click()
        loc7 = ("xpath",
                "//*[text()='八八A']")
        dengdai(self.driver, loc7).click()
        time.sleep(2)
        # time.sleep(20)
        # loactor =self.driver.find_element_by_xpath("//*[@id='text_list']/div[2]/table/tbody/tr[2]/td[4]").text
        # print(loactor)
        loactor = ("xpath", "//*[@id='text_list']/div[1]/table/tbody/tr[2]/td[9]/div")
        element1 = WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(loactor, ""))
        print(element1)
        assert element1  # 断言能不能获取 文本为空
#回迁房业务
    def testgg_33(self):
        '''回迁房业务-回迁房业务申请查询（职能）菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='回迁房业务']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '7db73932-8e3e-4f6e-9651-1cf65cc75311回迁房业务申请查询（职能）']")
        dengdai(self.driver, loc2).click()
        time.sleep(1)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_34(self):
        '''回迁房业务-回迁房业务申请查询（职能）菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='回迁房业务']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '13da29af-315d-4234-be6d-8466b065c04a回迁房业务查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        a = self.driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_35(self):
        '''预(销)售管理-回迁房业务受理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='回迁房业务']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        # js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        # self.driver.execute_script(js)
        # time.sleep(3)
        loc2 = ("xpath", "//*[@id = '0fc14666-47b0-462e-bc39-2d544a131b1f回迁房业务受理']")
        dengdai(self.driver, loc2).click()
        time.sleep(6)
        a = self.driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        # self.driver.find_element_by_xpath("//*[@id= 'BZ']").send_keys("20190903huiqian")
        self.driver.switch_to.frame("iframeslxx")
        loc3 = ("xpath", "//*[@id= 'BZ']")
        dengdai(self.driver, loc3).send_keys("20190903huiqian")  #
        # loc3 = ("xpath", "//*[@id= 'Btn_YY']")
        # dengdai(self.driver, loc3).click()  # 点引用模板按钮
        # loactor = ("xpath", "//iframe[starts-with(@src,'/spf/Htmbbg/htmbbgsqYymb?bid=')]")  # 切换iframe
        # WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id= 'Btn_YY']")
        dengdai(self.driver, loc3).click()  # 点引用楼盘
        time.sleep(3)
        self.driver.switch_to.default_content()
        a = self.driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'/Spf/HQF/hqf_yylp?bid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'selValue']")
        dengdai(self.driver, loc3).send_keys("广州万达广场有限公司1")  # 输入万达
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # self.driver.find_element_by_xpath("//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img").click()
        loc4 = ("xpath", "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img")
        dengdai(self.driver, loc4).click()  # 点公司
        loc5 = ("xpath", "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img")
        dengdai(self.driver, loc5).click()  # 点项目
        loc6 = ("xpath", "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img")
        dengdai(self.driver, loc6).click()  # 点自然幢
        loc7 = ("xpath", "//*[text()= '云浮海晴居A']")
        dengdai(self.driver, loc7).click()  # 点逻辑幢
        loc8 = ("xpath",
                "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/img")
        dengdai(self.driver, loc8).click()  # 点选左边
        time.sleep(5)
        loc9 = ("xpath", "//*[@onclick='checkedItem(this);']")  #选中
        dengdai(self.driver, loc9).click()
        self.driver.switch_to.default_content()
        time.sleep(3)
        loc10 = ("xpath", "//*[text()= '确定']")
        dengdai(self.driver, loc10).click()  # 点确定
        time.sleep(3)
        loactor = (
            "xpath", "//*[@class ='dhtmlx_popup_text']")  #
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "房号：103存在未办结的回迁房受理业务，不能引用！"))
        assert element1  # 断言能不能获取 103存在未办结的回迁房受理业务，不能引用！

    def testgg_36(self):
        '''预(销)售管理-回迁房业务变更受理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='回迁房业务']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '6e18d6d7-1769-46d7-8782-57aaec660c07回迁房业务变更受理']")
        dengdai(self.driver, loc2).click()
        time.sleep(6)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 300).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # self.driver.find_element_by_xpath("//*[@id= 'BZ']").send_keys("20190903huiqian")
        # loc3 = ("xpath", "//*[@id= 'Btn_YY']")
        # dengdai(self.driver, loc3).click()  # 点引用模板按钮
        # loactor = ("xpath", "//iframe[starts-with(@src,'/spf/Htmbbg/htmbbgsqYymb?bid=')]")  # 切换iframe
        # WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id= 'btnYylp']")
        dengdai(self.driver, loc3).click()  # 点引用引用回迁房
        time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'/Spf/HQF/hqfbgsqxx?bid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/Spf/HQF/hqfbgsqxx?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 300).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # loc3 = ("xpath", "//*[@id= 'selValue']")
        # dengdai(self.driver, loc3).send_keys("广州万达广场有限公司1")  # 输入万达
        loc3 = ("xpath", "//*[@class= 'buttonBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        # self.driver.find_element_by_xpath("//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img").click()

        loc9 = ("xpath", "//*[@name='yyfwxxRadio']")  # 选中
        dengdai(self.driver, loc9).click()
        self.driver.switch_to.parent_frame()
        time.sleep(3)
        loc10 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.myPrivate.YYFWXXSubmit();']")
        dengdai(self.driver, loc10).click()  # 点确定
        self.driver.switch_to.default_content()

        loactor = (
            "xpath", "//*[@class ='dhtmlx_popup_text']")  #
        element1 = WebDriverWait(self.driver, 200).until(
            EC.text_to_be_present_in_element(loactor, "该记录已被引用，不能重复引用！"))
        assert element1  # 断言能不能获取 103存在未办结的回迁房受理业务，不能引用！
        # self.driver.switch_to.parent_frame()
        # loc4 = ("xpath", "//*[@onclick = 'winModalDlg.getFrame().contentWindow.loadlist();']")
        # dengdai(self.driver, loc4).click()  # 点确定
        # time.sleep(20)
        # loc5 = ("xpath", "//*[@id= 'BZ']")
        # dengdai(self.driver, loc5).send_keys("20190830HTMBBG")  # 输入变更原因
        # loc6 = ("xpath", "//*[@id= 'btnSubmit']")
        # dengdai(self.driver, loc6).click()  # 点提交按钮
        # time.sleep(10)
        # loactor = ("xpath", "//iframe[starts-with(@src,'/SPF/Txyj/Txyj?ywid=')]")  # 切换iframe
        # WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # loc5 = ("xpath", "//*[@id= 'txtspyj']")
        # dengdai(self.driver, loc5).send_keys("20190830审核通过")  # 输入意见
        # self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # loc4 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.SubmitTxyj();']")
        # dengdai(self.driver, loc4).click()  # 点确定
        # time.sleep(30)
        # self.driver.switch_to.default_content()
        # # self.driver.find_element_by_xpath("//*[text()= '确定']")
        # # time.sleep(40)
        # # t = self.driver.find_element_by_xpath("//*[text()= '确定']").text
        # # print(t)
        # # assert  t
        # loactor = (
        #     "xpath", "//*[text()= '确定']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        # element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "确定"))
        # assert element1
#商品房合同管理
    def testgg_37(self):
        '''商品房合同管理-合同管理查询（职能）菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '822b3146-067f-45d4-bd0a-e1208bd205d3合同管理']")
        dengdai(self.driver, loc2).click()
        time.sleep(1)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 300).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc0 = ("xpath", "//*[@name= 'myQI_1']")
        dengdai(self.driver, loc0).send_keys("江东新区2019-000357") # 输入合同
        time.sleep(8)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 600).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_38(self):
        '''商品房合同管理-合同备案查询（职能）菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'a82e63d5-6d8c-4fa2-bb30-d4543e0ce15a合同备案查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        a = self.driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_39(self):
        '''商品房合同管理-合同注销查询（职能）菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '7ac2e9c0-8ccc-4921-80e5-20bab4111c93合同注销查询']")
        dengdai(self.driver, loc2).click()
        time.sleep(3)
        a = self.driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_40(self):
        '''商品房合同管理-合同统计（职能）菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'c9719bf7-883b-4610-9606-9e6935eb7932合同统计']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_41(self):
        '''商品房合同管理-购房资格审批查询（职能）菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '276778f3-02fb-44ae-ad27-bfacd27625c8购房资格审批查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='first disabled']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "首页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_42(self):
        '''商品房合同管理-购房资格作废（职能）菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '82f0fa13-1f0d-4d68-b177-6ad9e6e74275购房资格作废']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='first disabled']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "首页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_43(self):
        '''商品房合同管理-合同备案-申请查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '46300953-d45b-4a78-b1c4-0cc05b28d2c6合同备案-申请查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_44(self):
        '''商品房合同管理-商品房合同变更查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '9c8c1131-01f3-490b-84a1-8d37ac283b03商品房合同变更查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_45(self):
        '''商品房合同管理-待办业务菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'c7fc0ac5-f01f-4ac4-9707-25f3a8ce5c5b待办业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_46(self):
        '''商品房合同管理-已办业务查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '87173551-2035-464c-8740-9227fd588db5已办业务']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testgg_47(self):
        '''商品房合同管理-已备案合同变更查询菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '10b2ad8e-998a-40e2-9dab-373d57a2a9ed已备案合同变更查询']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页

    def testgg_48(self):
        '''商品房合同管理-合同备案受理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '0ee7dec1-77c2-4f9e-8168-fbda77db0e4c合同备案受理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(6)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # self.driver.find_element_by_xpath("//*[@id= 'BZ']").send_keys("20190903huiqian")
        loc3 = ("xpath", "//*[@class = 'dhxtoolbar_text'and text()= '引入合同']")
        dengdai(self.driver, loc3).click()  # 点引HTBH按钮
        loactor1 = ("xpath", "//iframe[starts-with(@src,'/spf/htba/CiteContract?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor1))
        loc3 = ("xpath", "//*[@id= 'txt_search']")
        dengdai(self.driver, loc3).send_keys("江东新区2019-000038")  # 输入HTBH
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(3)
        # self.driver.find_element_by_xpath("//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img").click()
        loc9 = ("xpath", "//*[@name='checkRadio']")  # 选中
        dengdai(self.driver, loc9).click()
        self.driver.switch_to.parent_frame()
        loc10 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.loadlist();']")
        dengdai(self.driver, loc10).click()  # 点确定
        time.sleep(2)
        self.driver.switch_to.default_content()
        loactor = (
            "xpath", "//*[@class ='dhtmlx_popup_text']")  #
        element1 = WebDriverWait(self.driver, 200).until(
            EC.text_to_be_present_in_element(loactor, "该合同正在办理备案业务！"))
        assert element1  # 断言

    def testgg_49(self):
        '''商品房合同管理-合同注销受理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'a6248f15-a1e2-4d2f-823f-d909b008af18合同注销受理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class = 'dhxtoolbar_text'and text()= '引入合同']")
        dengdai(self.driver, loc3).click()  # 点引HTBH按钮
        loactor1 = ("xpath", "//iframe[starts-with(@src,'/spf/htba/CiteContract?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor1))
        loc3 = ("xpath", "//*[@id= 'txt_search']")
        dengdai(self.driver, loc3).send_keys("江东新区2019-000368")  # 输入HTBH
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # self.driver.find_element_by_xpath("//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img").click()
        loc9 = ("xpath", "//*[@name='checkRadio']")  # 选中
        dengdai(self.driver, loc9).click() # 选中
        self.driver.switch_to.parent_frame()
        loc10 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.loadlist();']")
        dengdai(self.driver, loc10).click()  # 点确定
        time.sleep(2)
        self.driver.switch_to.default_content()
        # t = self.driver.find_element_by_xpath("//*[@class ='dhtmlx_popup_text']").text
        # print(t)
        loactor = ("xpath", "//*[@class ='dhtmlx_popup_text']")  #
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "房屋状态为抵押 ，不可引用该合同"))
        assert element1  # 断言

    def testgg_50(self):
        '''商品房合同管理-商品房合同变更受理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '6707d2d4-e537-43ec-8ddb-4823cd15369c商品房合同变更受理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class = 'dhxtoolbar_text'and text()= '引入合同']")
        dengdai(self.driver, loc3).click()  # 点引HTBH按钮
        loactor1 = ("xpath", "//iframe[starts-with(@src,'/spf/htba/htbasqYyht?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor1))
        loc3 = ("xpath", "//*[@id= 'txt_search']")
        dengdai(self.driver, loc3).send_keys("江东新区2019-000368")  # 输入HTBH
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # self.driver.find_element_by_xpath("//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img").click()
        loc9 = ("xpath", "//*[@name='checkRadio']")  # 选中
        dengdai(self.driver, loc9).click()  # 选中
        self.driver.switch_to.parent_frame()
        loc10 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.loadlist();']")
        dengdai(self.driver, loc10).click()  # 点确定
        time.sleep(2)
        self.driver.switch_to.default_content()
        # t = self.driver.find_element_by_xpath("//*[@class ='dhtmlx_popup_text']").text
        # print(t)
        loactor = ("xpath", "//*[@class ='dhtmlx_popup_text']")  #
        element1 = WebDriverWait(self.driver, 200).until(
            EC.text_to_be_present_in_element(loactor, "房屋状态为抵押 ，不可引用该合同"))
        assert element1  # 断言

    def testgg_51(self):
        '''商品房合同管理-已备案合同注销受理菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='商品房合同管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = '411c7e9a-84ca-453c-bbc9-7dc68cc1872e已备案合同注销受理']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class = 'dhxtoolbar_text'and text()= '引入合同']")
        dengdai(self.driver, loc3).click()  # 点引HTBH按钮
        loactor1 = ("xpath", "//iframe[starts-with(@src,'/spf/htba/CiteContract?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor1))
        loc3 = ("xpath", "//*[@id= 'txt_search']")
        dengdai(self.driver, loc3).send_keys("江东新区2019-000368")  # 输入HTBH
        loc3 = ("xpath", "//*[@id= 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        # self.driver.find_element_by_xpath("//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img").click()
        loc9 = ("xpath", "//*[@name='checkRadio']")  # 选中
        dengdai(self.driver, loc9).click()  # 选中
        self.driver.switch_to.parent_frame()
        loc10 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.loadlist();']")
        dengdai(self.driver, loc10).click()  # 点确定
        self.driver.switch_to.default_content()
        loc3 = ("xpath", "//*[text()= '确定']")
        dengdai(self.driver, loc3).click()  #点确定
        time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # t = self.driver.find_element_by_xpath("//*[@class ='dhtmlx_popup_text']").text
        # print(t)
        loactor = ("xpath", "//*[@id='ywspBase_content']/div/div/div/div[1]")  #
        element1 = WebDriverWait(self.driver, 200).until( EC.text_to_be_present_in_element(loactor, "业务受理信息"))
        assert element1  # 断言

    # def testgg_52(self):    #有问题要调试
    #     '''商品房合同管理-合同补录菜单查询功能'''
    #     # self.driver = webdriver.Firefox()
    #     # loginxt(self.driver, "lx022002", "lx022002")
    #     time.sleep(3)
    #     loc1 = ("xpath", "//*[text()='商品房合同管理']")
    #     dengdai(self.driver, loc1).click()
    #     time.sleep(1)
    #     js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 600;'
    #     self.driver.execute_script(js)
    #     time.sleep(3)
    #     loc2 = ("xpath", "//*[@id = 'b37d87e5-83a2-46fe-a21e-cd66f73db4f1合同补录']")
    #     dengdai(self.driver, loc2).click()
    #     loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
    #     WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
    #     loc3 = ("xpath", "//*[@class = 'dhxtoolbar_text'and text()= '引用楼盘']")
    #     dengdai(self.driver, loc3).click()  # 点引引用楼盘按钮
    #     loc3 = ("xpath", "//*[@id= 'txt_qymc']")
    #     dengdai(self.driver, loc3).send_keys("广州天地有限公司")  # 输入企业名称
    #     loc4 = ("xpath", "//*[@id= 'txt_xmmc']")
    #     dengdai(self.driver, loc4).send_keys("万达")# 输入项目名称
    #     loc5 = ("xpath", "//*[@id= 'txt_zrzmc']")
    #     dengdai(self.driver, loc5).send_keys("清远万达A")  # 输入自然幢名称
    #     loc6 = ("xpath", "//*[@id= 'txt_fh']")
    #     time.sleep(3)
    #     dengdai(self.driver, loc6).send_keys("202")  # 输入房号
    #     loc7 = ("xpath", "//*[@id= 'btn_search']")
    #     dengdai(self.driver, loc7).click()  #点查询
    #     time.sleep(3)
    #     loc8 = ("xpath", "//*[@id='gridbox_jgzhgl']/div[2]/table/tbody/tr[2]/td[1]/label/input")  #    //*[@class= 'checkall']
    #     dengdai(self.driver, loc8).click()  # 点选中
    #     time.sleep(3)
    #     loc8 = ("xpath", "//*[@class = 'dhxtoolbar_text'and text()= '保存']")
    #     dengdai(self.driver, loc8).click()  # 点保存
    #     time.sleep(5)
    #     self.driver.switch_to.default_content()
    #     loactor = ("xpath", "//*[@class='fieldset-title']")  #
    #     element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "基本信息"))
    #     assert element1  # 断言
#同步日志管理
    def testgg_53(self):
        '''同步日志管理-江门推送PDF合同日志查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(2)
        loc1 = ("xpath", "//*[text()='同步日志管理']")
        dengdai(self.driver, loc1).click()
        time.sleep(1)
        js = 'document.getElementsByClassName("dhxacc_cont")[0].scrollTop = 800;'
        self.driver.execute_script(js)
        time.sleep(3)
        loc2 = ("xpath", "//*[@id = 'c6d08ed4-44d9-4c17-a382-cda43f053a74江门推送PDF合同日志']")
        dengdai(self.driver, loc2).click()
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath(
        #     "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(2)
        # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        loactor = (
            "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页


































        # loc3 = ("xpath", "//*[@id= 'txt_search']")
        # dengdai(self.driver, loc3).send_keys("江东新区2019-000368")  # 输入HTBH
        # loc3 = ("xpath", "//*[@id= 'btn_search']")
        # dengdai(self.driver, loc3).click()  # 点查询
        # # self.driver.find_element_by_xpath("//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img").click()
        # loc9 = ("xpath", "//*[@name='checkRadio']")  # 选中
        # dengdai(self.driver, loc9).click()  # 选中
        # self.driver.switch_to.parent_frame()
        # loc10 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.loadlist();']")
        # dengdai(self.driver, loc10).click()  # 点确定
        # self.driver.switch_to.default_content()
        # loc3 = ("xpath", "//*[text()= '确定']")
        # dengdai(self.driver, loc3).click()  # 点确定
        # loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # # t = self.driver.find_element_by_xpath("//*[@class ='dhtmlx_popup_text']").text
        # # print(t)
        # loactor = ("xpath", "//*[@id='ywspBase_content']/div/div/div/div[1]")  #
        # element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "业务受理信息"))
        # assert element1  # 断言
















        # # loactor = self.driver.find_element_by_xpath("//*[@class ='dataTable_TY btn btn-small btn-primary']").text
        # loactor = (
        #     "xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")  # "//*[@id='cxlb_pagingArea']/div/div[9]"
        # element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        # assert element1  # 断言能不能获取 跳页
    #
        #
        #
        # time.sleep(3)
        # loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")   #"//*[@id='cxlb_pagingArea']/div/div[9]"
        # element1 = WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        # assert element1  # 断言能不能获取 跳页
