#@Author: LIUXIANG
#@Time  :  2019/8/21 8:17
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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

class CxglJiekou(unittest.TestCase):
    '''职能端诚信管理系统各查询，引用，调档接口测试'''
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.driver = webdriver.Firefox()
    #     loginxt1(cls.driver)
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        loginxt(self.driver, "lx022002", "lx022002")
        loc1 = ("xpath", "//*[text()='诚信管理']")
        dengdai(self.driver, loc1).click()
    def tearDown(self) -> None:
        self.driver.close() #关闭当前窗口
    # def setUp(self) -> None:

    def testcxgl_01(self):
        '''诚信管理，开发商奖惩积分规则菜单查询功能'''
        # self.driver.find_element_by_xpath("//*[text()='诚信管理']").click()
        # self.driver.find_element_by_xpath("//*[@id = 'dae19884-2b83-4dfd-a856-e380db261de0开发商奖惩积分规则']").click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'dae19884-2b83-4dfd-a856-e380db261de0开发商奖惩积分规则']")
        dengdai(self.driver, loc2).click()  # 点开发商奖惩积分规则菜单
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # loc = ("xpath", "//*[@id='txt_search']")
        # dengdai(self.driver, loc).send_keys("05051")  # 输入规则名称
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_02(self):
        '''诚信管理，开发商诚信管理菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '07b141c1-92e6-4546-9871-354c04bb706d开发商诚信管理']")
        dengdai(self.driver, loc2).click()  # 点开发商奖惩积分规则菜单
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//*[@id = '07b141c1-92e6-4546-9871-354c04bb706d开发商诚信管理']").click()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_03(self):
        '''诚信管理，开发商诚信统计菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '25b3fa5c-574f-4f47-9d65-19559a0720a1开发商诚信统计']")
        dengdai(self.driver, loc2).click()  # 点开发商奖惩积分规则菜单
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_04(self):
        '''诚信管理，物业服务奖惩积分规则菜单查询功能'''
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'e3cb7d08-6042-4b7c-962a-4c8775d69b5a物业服务奖惩积分规则']")
        dengdai(self.driver, loc2).click()  # 点开发商奖惩积分规则菜单
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_05(self):
        '''诚信管理，物业服务诚信管理菜单查询功能'''
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'f20c2eb8-1dca-46fb-bed0-232e2c2a3c38物业服务诚信管理']")
        dengdai(self.driver, loc2).click()  # 点开发商奖惩积分规则菜单
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath( "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_06(self):
        '''诚信管理，物业服务诚信统计菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '5d187106-f3ce-44fe-a944-4126623158ab物业服务诚信统计']")
        dengdai(self.driver, loc2).click()  # 点物业服务诚信统计
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_07(self):
        '''诚信管理，诚信等级管理菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '15f45e73-ccfc-448a-8d6a-30e85585d80d诚信等级管理']")
        dengdai(self.driver, loc2).click()  # 点诚信等级管理
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@onclick = 'return selectButton(event)']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_08(self):
        '''诚信管理，经纪机构奖惩积分规则菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '97669e4d-3f5f-4bb8-b987-37bb7124f9de经纪机构奖惩积分规则']")
        dengdai(self.driver, loc2).click()  # 点开发商奖惩积分规则菜单
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath( "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_09(self):
        '''诚信管理，经纪机构诚信管理菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '0757465b-e79b-410a-9c77-192c108ce7c7经纪机构诚信管理']")
        dengdai(self.driver, loc2).click()  # 点开发商奖惩积分规则菜单
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_10(self):
        '''诚信管理，经纪机构诚信统计菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'f21a05b8-137e-452c-a8b3-866d5d0b0f41经纪机构诚信统计']")
        dengdai(self.driver, loc2).click()  # 点开发商奖惩积分规则菜单
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_11(self):
        '''诚信管理，诚信奖罚业务查询-清远菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '96c55544-9d2a-4391-9d68-01758c382104诚信奖罚业务查询-清远']")
        dengdai(self.driver, loc2).click()  # 点开发商奖惩积分规则菜单
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class='myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_12(self):
        '''诚信管理，诚信上诉业务查询菜单查询功能'''

        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'cc20394d-6278-403b-83c5-59c1ed9ed923诚信上诉业务查询']")
        dengdai(self.driver, loc2).click()  #
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class='myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_13(self):
        '''诚信管理，安全鉴定机构奖惩积分规则菜单查询功能'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '73359f25-4cac-4701-8d7e-170743c15341安全鉴定机构奖惩积分规则']")
        dengdai(self.driver, loc2).click()  # 点
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_14(self):
        '''诚信管理，安全鉴定机构诚信管理菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'a69f88e0-e209-429c-80ec-9c51e7d1ed60安全鉴定机构诚信管理']")
        dengdai(self.driver, loc2).click()  # 点
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_15(self):
        '''诚信管理，安全鉴定机构诚信统计菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'e8788c75-efcd-448a-99bc-d7e79f2aaba8安全鉴定机构诚信统计']")
        dengdai(self.driver, loc2).click()  # 点
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_16(self):
        '''诚信管理，诚信加分业务查询菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '3b3d9152-3210-4f5a-94d9-e25a1db69901诚信加分业务查询']")
        dengdai(self.driver, loc2).click()  # 点诚信加分业务查询
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='c']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_17(self):
        '''诚信管理，不良记录查询菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'ea45ef33-b998-48ad-ab29-3042bd454385不良记录查询']")
        dengdai(self.driver, loc2).click()  # 点不良记录查询
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='c']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_18(self):
        '''诚信管理，鉴定企业诚信评分规则管理菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'fde4e90f-06a3-4a25-8a37-5de5c0875512鉴定企业诚信评分规则管理']")
        dengdai(self.driver, loc2).click()  # 点不良记录查询
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id='btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver,40).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_19(self):
        '''诚信管理，诚信等级管理（云浮）菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '7ffe478a-69e3-42dd-88e5-800fa8065bdb诚信等级管理（云浮）']")
        dengdai(self.driver, loc2).click()  # 点诚信等级管理（云浮）
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@onclick = 'return selectButton(event)']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_20(self):
        '''诚信管理，诚信行为记录（云浮）菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '21ce7886-a41e-4d47-ac71-3aecf2f2698f诚信行为记录（云浮）']")
        dengdai(self.driver, loc2).click()  # 点诚信行为记录（云浮）
        # time.sleep(4)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class = 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_21(self):
        '''诚信管理，诚信申诉业务查询菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '5d15d92a-e2f4-4316-b3f4-050f2e7e927d诚信申诉业务查询']")
        dengdai(self.driver, loc2).click()  # 点诚信申诉业务查询
        # time.sleep(4)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class = 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_22(self):
        '''诚信管理，诚信行为记录查询（云浮）菜单查询功能'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '55e91c49-e818-48e0-be08-799954194331诚信行为记录查询（云浮）']")
        dengdai(self.driver, loc2).click()  # 点诚信行为记录查询（云浮）
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class = 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_23(self):
        '''诚信管理，企业抽查记录（云浮）菜单查询功能'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'd84044f7-2672-4e1d-b8fd-6a70b76529ea企业抽查记录（云浮）']")
        dengdai(self.driver, loc2).click()  # 点企业抽查记录（云浮）
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class = 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_24(self):
        '''诚信管理，企业抽查记录（云浮）菜单查询功能'''
        time.sleep(2)
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        loc2 = ("xpath", "//*[@id = 'd84044f7-2672-4e1d-b8fd-6a70b76529ea企业抽查记录（云浮）']")
        dengdai(self.driver, loc2).click()  # 点企业抽查记录（云浮）
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class = 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_25(self):
        '''诚信管理，诚信管理（云浮）菜单查询功能'''
        time.sleep(2)
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        loc2 = ("xpath", "//*[@id = '3e642c38-6e7d-4a06-9f46-0f7a22cfd47f诚信管理（云浮）']")
        dengdai(self.driver, loc2).click()  # 点诚信管理（云浮）
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_26(self):
        '''诚信管理，企业黑名单管理（云浮）菜单查询功能'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '90b5c2d5-d0a8-4277-a89b-0f933e6fc987企业黑名单管理（云浮）']")
        dengdai(self.driver, loc2).click()  # 点企业黑名单管理（云浮）
        # time.sleep(4)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_27(self):
        '''诚信管理，诚信档案统计功能菜单查询功能'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '6a89297a-fdce-4a80-bced-fc60cec74e10诚信档案统计功能']")
        dengdai(self.driver, loc2).click()  # 点诚信档案统计功能
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class = 'buttonBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(6)
        t = self.driver.find_element_by_xpath("//*[@class ='hdrcell'and text()= '企业名称']").text
        # print(t)
        assert t
         # 断言能不能获取 企业名称
    def testcxgl_28(self):
        '''诚信管理，物业协会菜单查询功能'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '73483dc8-12ea-4444-b8c4-e43f36604e00物业协会']")
        dengdai(self.driver, loc2).click()  # 点物业协会
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_29(self):
        '''诚信管理，诚信建档查询功能'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '46ea7fdb-7e0f-4dea-b1ba-d2cb6025ed28诚信建档查询']")
        dengdai(self.driver, loc2).click()  # 点诚信建档查询
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'btn_search']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_30(self):
        '''诚信管理，诚信记录业务查询功能'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '729e0097-d2a2-4071-9092-23b74d5043cb诚信记录业务查询']")
        dengdai(self.driver, loc2).click()  # 点诚信记录业务查询
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_31(self):
        '''诚信管理，诚信行为记录查询查询功能'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '30bd6877-bdb5-4d11-9866-dd94abca38f1诚信行为记录查询']")
        dengdai(self.driver, loc2).click()  # 点诚信行为记录查询
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class= 'myQueryBtn']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_32(self):
        '''诚信管理，诚信等级管理-江门查询功能'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'b536bb11-93f3-42a7-a317-6029418e97f8诚信等级管理-江门']")
        dengdai(self.driver, loc2).click()  # 点诚信等级管理-江门
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@class= 'addButton' and @onclick= 'return selectButton(event)']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_33(self):
        '''诚信管理，诚信红黑榜查询功能'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'b61c978d-1eba-4040-b155-6cc9a610262b诚信红黑榜']")
        dengdai(self.driver, loc2).click()  # 点诚信红黑榜
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        # time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id= 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@id='gridbox_datalist']/div[1]/table/tbody/tr[2]/td[2]")
        # loactor = self.driver.find_element_by_xpath("//*[@id='gridbox_datalist']/div[1]/table/tbody/tr[2]/td[2]").text
        # print(loactor)
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "诚信红榜企业"))
        assert element1  # 断言能不能获取 跳页
    def testcxgl_34(self):
        '''诚信管理，失信行为申报受理-江门菜单查询,引用企业接口'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '9f8171a3-4819-4d43-b903-7d87289878ed失信行为申报受理-江门']")
        dengdai(self.driver, loc2).click()  # 点失信行为申报受理-江门
        time.sleep(5)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        # time.sleep(4)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@id = 'btnYYQY']")  # 引用按钮
        dengdai(self.driver, loac3).click()  # 点引用按钮
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/Spf/SincerityJM/CXJJFYWSLZN_YYQY?bid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/Spf/SincerityJM/CXJJFYWSLZN_YYQY?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # loac4 = ("xpath", "//*[@name = 'xctj_value']")  # s输入企业名称
        # dengdai(self.driver, loac4).send_keys("河源市大众房地产开发有限公司")
        loac3 = ("xpath", "//*[@class = 'buttonBtn']")  # 查询按钮
        dengdai(self.driver, loac3).click()  #
        time.sleep(2)
        loac5 = ("name", "yyfwxxRadio")
        dengdai(self.driver, loac5).click()  # 选择单选
        # self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        self.driver.switch_to.parent_frame()
         # loac6 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.myPrivate.YYFWXXSubmit();']")  # 确定按钮
        loac6 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.myPrivate.YYFWXXSubmit();']")
        dengdai(self.driver, loac6).click()  # 确定按钮
        time.sleep(3)
        self.driver.switch_to.default_content()
        loactor = ("xpath", "//*[@class='dhtmlx_popup_text']")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "当前企业已有在办奖罚业务了"))
        assert element4

        # dengdai(self.driver, loac6).click()  # 点击确定按钮
        # time.sleep(2)
        # self.driver.switch_to.frame("iframeslxx")
        # time.sleep(5)
        # # 方法2
        # # loactor= self.driver.find_element_by_xpath("//*[@id='formbox']/tr[1]/th[1]").text
        # # print(loactor)
        # # assert loactor
        # loactor = ("xpath", "//*[@id='formbox']/tr[1]/th[1]")
        # element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "受理号："))
        # assert element4
        time.sleep(2)
    def testcxgl_35(self):
        '''诚信管理，诚信批量加减分受理菜单查询受理接口'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '65e43aee-5b7e-461c-8f42-11de9cf20b81诚信批量加减分受理']")
        dengdai(self.driver, loc2).click()  # 点诚信批量加减分受理
        time.sleep(8)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@id = 'btnYYQY']")  # 引用按钮
        dengdai(self.driver, loac3).click()  # 点引用按钮
        # time.sleep(4)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/Spf/Sincerity/CXJJFYWSLZN_YYQY?bid=')]")
        # self.driver.switch_to.frame
        loactor = ("xpath", "//iframe[starts-with(@src,'/Spf/Sincerity/CXJJFYWSLZN_YYQY?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@class = 'buttonBtn']")  # 查询按钮
        dengdai(self.driver, loac3).click()  #
        loac5 = ("name", "yyfwxxRadio")
        dengdai(self.driver, loac5).click()  # 选择单选
        # self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        self.driver.switch_to.parent_frame()
        loac6 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.myPrivate.YYFWXXSubmit();']")  # 确定按钮
        time.sleep(2)
        dengdai(self.driver, loac6).click()  # 点击确定按钮
        self.driver.switch_to.default_content()  # 回到默认顶层
        time.sleep(3)
        loactor = ("xpath", "//*[@class='dhtmlx_popup_text']")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "当前企业已有在办奖罚业务了"))
        assert element4
        # time.sleep(5)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        # self.driver.switch_to.frame("iframeslxx")
        # time.sleep(5)
        # # 方法2
        # # loactor= self.driver.find_element_by_xpath("//*[@id='formbox']/tr[1]/th[1]").text
        # # print(loactor)
        # loactor = ("xpath", "//*[@id='formbox']/tr[1]/th[1]")
        # element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "受理号："))
        # assert element4
        # time.sleep(2)
    def testcxgl_36(self):
        '''诚信管理，诚信减分受理(清远)菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = 'c4561b62-abd6-4fd7-a7d8-ea7cefc377ba诚信减分受理(清远)']")
        dengdai(self.driver, loc2).click()  # 点诚信减分受理(清远)
        time.sleep(6)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        # time.sleep(4)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@id = 'btnYYQY']")  # 引用按钮
        dengdai(self.driver, loac3).click()  # 点引用按钮
        loactor = ("xpath", "//iframe[starts-with(@src,'/Spf/Sincerity/CXJJFYWSLZN_YYQY?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # time.sleep(4)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/Spf/Sincerity/CXJJFYWSLZN_YYQY?bid=')]")
        # self.driver.switch_to.frame(a)
        loac1 = ("xpath", "//*[@id = 'QYMC']")  # 查询按钮
        dengdai(self.driver, loac1).send_keys("河源市咏明房地产开发有限公司")
        loac3 = ("xpath", "//*[@class = 'buttonBtn']")  # 查询按钮
        dengdai(self.driver, loac3).click()  #
        loac5 = ("name", "yyfwxxRadio")
        dengdai(self.driver, loac5).click()  # 选择单选
        # self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        self.driver.switch_to.parent_frame()
        loac6 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.myPrivate.YYFWXXSubmit();']")  # 确定按钮
        time.sleep(2)
        dengdai(self.driver, loac6).click()  # 点击确定按钮
        self.driver.switch_to.default_content()  # 回到默认顶层
        time.sleep(3)
        loactor = ("xpath", "//*[@class='dhtmlx_popup_text']")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "当前企业已有在办奖罚业务了"))
        assert element4
        # time.sleep(5)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        # self.driver.switch_to.frame("iframeslxx")
        # time.sleep(2)
        # # 方法2
        # # loactor= self.driver.find_element_by_xpath("//*[@id='formbox']/tr[1]/th[1]").text
        # # print(loactor)
        # loactor = ("xpath", "//*[@id='formbox']/tr[1]/th[1]")
        # element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "受理号："))
        # assert element4
        # time.sleep(2)
    # def testcxgl_37(self):   该流程已停用
    #     '''诚信管理，诚信行为申报受理-江门菜单查询,引用企业接口'''
    #     #
    #     # loc1 = ("xpath", "//*[text()='诚信管理']")
    #     # dengdai(self.driver, loc1).click()
    #     time.sleep(2)
    #     e = "河源市和禄房地产开发有限公司"# s输入企业名称
    #     loc2 = ("xpath", "//*[@id = '5fdddfcd-44f5-4182-bdf0-26e7d991c581诚信行为申报受理-江门']")
    #     dengdai(self.driver, loc2).click()  # 点诚信行为申报受理-江门
    #     time.sleep(6)
    #     # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
    #     # self.driver.switch_to.frame(a)
    #     # time.sleep(4)
    #     loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
    #     WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
    #     loac3 = ("xpath", "//*[@id = 'btnYYQY']")  # 引用按钮
    #     dengdai(self.driver, loac3).click()  # 点引用按钮
    #     # time.sleep(3)
    #     # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/Spf/SincerityJM/CXJJFYWSLZN_YYQY?bid=')]")
    #     # self.driver.switch_to.frame(a)
    #     loactor = ("xpath", "//iframe[starts-with(@src,'/Spf/SincerityJM/CXJJFYWSLZN_YYQY?bid=')]")  # 切换iframe
    #     WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
    #     loac4 = ("xpath", "//*[@id = 'QYMC']")  # s输入企业名称
    #     dengdai(self.driver, loac4).send_keys(e)
    #     loac3 = ("xpath", "//*[@class = 'buttonBtn']")  # 查询按钮
    #     dengdai(self.driver, loac3).click()  #
    #     loac5 = ("name", "yyfwxxRadio")
    #     dengdai(self.driver, loac5).click()  # 选择单选
    #     # self.driver.switch_to.default_content()
    #     # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
    #     # self.driver.switch_to.frame(a)
    #     self.driver.switch_to.parent_frame()
    #     loac6 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.myPrivate.YYFWXXSubmit();']")  # 确定按钮
    #     time.sleep(2)
    #     dengdai(self.driver, loac6).click()  # 点击确定按钮
    #     time.sleep(2)
    #     time.sleep(3)
    #     self.driver.switch_to.default_content()
    #     loactor = ("xpath", "//*[@class='dhtmlx_popup_text']")
    #     element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "当前企业已有在办奖罚业务了"))
    #     assert element4
    #
    def testcxgl_38(self):
        '''诚信管理，失信行为申报受理-江门菜单查询,引用企业接口'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        e = "深圳市新东江实业有限公司"  # 企业名称
        loc2 = ("xpath", "//*[@id = '9f8171a3-4819-4d43-b903-7d87289878ed失信行为申报受理-江门']")
        dengdai(self.driver, loc2).click()  # 点失信行为申报受理
        time.sleep(5)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        # time.sleep(4)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@id = 'btnYYQY']")  # 引用按钮
        dengdai(self.driver, loac3).click()  # 点引用按钮
        # time.sleep(3)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/Spf/SincerityJM/CXJJFYWSLZN_YYQY?bid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/Spf/SincerityJM/CXJJFYWSLZN_YYQY?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac4 = ("xpath", "//*[@name = 'xctj_value']")  # s输入企业名称
        dengdai(self.driver, loac4).send_keys(e)  # s输入企业名称
        loac3 = ("xpath", "//*[@class = 'buttonBtn']")  # 查询按钮
        dengdai(self.driver, loac3).click()  #
        loac5 = ("name", "yyfwxxRadio")
        dengdai(self.driver, loac5).click()  # 选择单选
        # self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        self.driver.switch_to.parent_frame()
        loac6 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.myPrivate.YYFWXXSubmit();']")  # 确定按钮
        time.sleep(2)
        dengdai(self.driver, loac6).click()  # 点击确定按钮
        time.sleep(2)
        self.driver.switch_to.default_content()
        loactor = ("xpath", "//*[@class='dhtmlx_popup_text']")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "当前企业已有在办奖罚业务了"))
        assert element4
        # # self.driver.switch_to.default_content()  # 回到默认顶层
        # # time.sleep(5)
        # # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # # self.driver.switch_to.frame(a)
        # self.driver.switch_to.frame("iframeslxx")
        # time.sleep(5)
        # # 方法2
        # # loactor= self.driver.find_element_by_xpath("//*[@id='formbox']/tr[1]/th[1]").text
        # # print(loactor)
        # # assert loactor
        # loactor = ("xpath", "//*[@id='formbox']/tr[1]/th[1]")
        # element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "受理号："))
        # assert element4
        # time.sleep(2)
    def testcxgl_39(self):
        '''诚信管理，异议申请受理-江门菜单查询,引用企业接口'''
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        e = "江门四四有限公司"
        loc2 = ("xpath", "//*[@id = '0fb3459a-c4fe-4916-a0a0-24203c82cfbe异议申请受理-江门']")
        dengdai(self.driver, loc2).click()  # 点异议申请受理-江门
        time.sleep(5)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        # time.sleep(4)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@id = 'btnYY']")  # 引用按钮
        dengdai(self.driver, loac3).click()  # 点引用按钮
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/Spf/SincerityJM/CXJFSSYWSLZN_YYQY?bid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/Spf/SincerityJM/CXJFSSYWSLZN_YYQY?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac4 = ("xpath", "//*[@id = 'QYMC']")  # s输入企业名称
        dengdai(self.driver, loac4).send_keys(e)
        loac3 = ("xpath", "//*[@id = 'btn_search']")  # 查询按钮
        dengdai(self.driver, loac3).click()  #
        loac5 = ("name", "yyfwxxRadio")
        dengdai(self.driver, loac5).click()  # 选择单选
        # self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        self.driver.switch_to.parent_frame()
        loac6 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.myPrivate.YYXXSubmit();']")  # 确定按钮
        dengdai(self.driver, loac6).click()  # 点击确定按钮
        time.sleep(3)
        self.driver.switch_to.default_content()
        loactor = ("xpath", "//*[@class='dhtmlx_popup_text']")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "该引用信息已在受理审批中。"))
        assert element4
        # time.sleep(2)
        # # self.driver.switch_to.default_content()  # 回到默认顶层
        # # time.sleep(5)
        # # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # # self.driver.switch_to.frame(a)
        # self.driver.switch_to.frame("iframeslxx")
        # time.sleep(5)
        # # 方法2
        # # loactor= self.driver.find_element_by_xpath("//*[@id='formbox']/tr[1]/th[1]").text
        # # print(loactor)
        # # assert loactor
        # loactor = ("xpath", "//*[@id='formbox']/tr[1]/th[1]")
        # element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "受理号："))
        # assert element4
        # time.sleep(2)
    def testcxgl_40(self):
        '''从业主体管理，诚信上诉业务受理菜单引用企业接口'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        e = "河源市桃花源房地产开发有限公司"  # 输入企业名称
        loc2 = ("xpath", "//*[@id = 'b68b7b9b-8c4f-4697-bb8a-6c74b0c9cffc诚信上诉业务受理']")
        dengdai(self.driver, loc2).click()  # 点
        time.sleep(5)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        # time.sleep(4)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@id = 'btnYYCFSJJL']")  # 引用按钮
        dengdai(self.driver, loac3).click()  # 点引用按钮
        # time.sleep(6)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/Spf/Sincerity/CFJJMXYYZN?bid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/Spf/Sincerity/CFJJMXYYZN?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@id = 'QYMC']")  # 查询按钮
        time.sleep(2)
        dengdai(self.driver, loac3).send_keys(e)  # 输入企业名称
        loac4 = ("xpath", "//*[@id = 'btnSearch']")  # 查询按钮
        time.sleep(2)
        dengdai(self.driver, loac4).click()
        loac5 = ("name", "yyfwxxRadio")
        dengdai(self.driver, loac5).click()  # 选择单选
        self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac6 = ("xpath", "//*[@onclick= 'winModalDlg.getFrame().contentWindow.myPrivate.YYXXSubmit();']")  # 确定按钮
        time.sleep(2)
        dengdai(self.driver, loac6).click()  # 点击确定按钮
        self.driver.switch_to.default_content()
        loactor = ("xpath", "//*[@class='dhtmlx_popup_text']")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "该引用信息已在受理审批中。"))
        assert element4
        # self.driver.switch_to.default_content()  # 回到默认顶层
        # time.sleep(5)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        # self.driver.switch_to.frame("iframeslxx")
        # time.sleep(5)
        # # 方法2
        # # loactor= self.driver.find_element_by_xpath("//*[@id='formbox']/tr[1]/th[1]").text
        # # print(loactor)
        # loactor = ("xpath", "//*[@id='formbox']/tr[1]/th[1]")
        # element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "受理号："))
        # assert element4
        # time.sleep(2)
    def testcxgl_41(self):
        '''诚信管理，诚信建档补录菜单查询,引用企业接口'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        e = "四季常青"# s输入企业名称
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '73e399dd-b41d-4f2a-b316-6193dc897686诚信建档补录']")
        dengdai(self.driver, loc2).click()  # 点诚信建档补录
        time.sleep(5)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        # time.sleep(4)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@id = 'btnCite']")  # 引用按钮
        dengdai(self.driver, loac3).click()  # 点引用按钮
        time.sleep(2)
        self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/SPF/cyqygl/ZZZSZXYY?bid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/SPF/cyqygl/ZZZSZXYY?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac4 = ("xpath", "//*[@id = 'keyword']")  # s输入企业名称
        dengdai(self.driver, loac4).send_keys(e)
        loac3 = ("xpath", "//*[@id = 'btnSearch']")  # 查询按钮
        dengdai(self.driver, loac3).click()  #
        loac5 = ("name", "QYID")
        dengdai(self.driver, loac5).click()  # 选择单选
        # self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        self.driver.switch_to.parent_frame()  # 回到上一层
        loac6 = ("xpath", "//*[@class= 'ui-dialog-autofocus']")  # 确定按钮
        dengdai(self.driver, loac6).click()  # 点击确定按钮  成功
        time.sleep(3)
        # self.driver.find_element_by_xpath("//*[text()= 'OK']").click()
        self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/SPF/cyqygl/ZZZSZXYY?bid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/SPF/cyqygl/ZZZSZXYY?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loactor = ("xpath", "//*[@class='dhtmlx_popup_text']")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "当前企业已有在办建档业务了！"))
        assert element4
        # self.driver.switch_to.default_content()  # 回到默认顶层
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        # # a = self.driver.find_element_by_xpath("//*[@id='index']/div[4]/div[2]/div[2]/div/div/div/div[6]/div/iframe")
        # # self.driver.switch_to.frame(a)
        # time.sleep(3)
        # # 方法2
        # # loactor= self.driver.find_element_by_xpath("//*[@id='formbox']/tr[1]/th[1]").text
        # # print(loactor)
        # # assert loactor
        # loactor = ("xpath", "//*[@id='formbox']/tr[1]/th[1]")
        # element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "受理号："))
        # assert element4
        # time.sleep(2)
    def testcxgl_42(self):
        '''诚信管理，诚信建档受理菜单查询,引用企业接口'''
        #
        # loc1 = ("xpath", "//*[text()='诚信管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(2)
        # e = "江门三三有限公司"
        loc2 = ("xpath", "//*[@id = '567f7294-6dcb-49e8-adc8-03f7563e41d3诚信建档受理']")
        dengdai(self.driver, loc2).click()  # 点诚信诚信建档受理
        # time.sleep(5)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        time.sleep(2)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        time.sleep(2)
        loac3 = ("xpath", "//*[@id = 'btnCite']")  # 引用按钮
        dengdai(self.driver, loac3).click()  # 点引用按钮
        time.sleep(2)
        self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/SPF/cyqygl/ZZZSZXYY?bid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/SPF/cyqygl/ZZZSZXYY?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac4 = ("xpath", "//*[@id = 'keyword']")  # s输入企业名称
        dengdai(self.driver, loac4).send_keys("河源市咏明房地产开发有限公司")
        loac3 = ("xpath", "//*[@id = 'btnSearch']")  # 查询按钮
        dengdai(self.driver, loac3).click()  #
        loac5 = ("name", "QYID")
        dengdai(self.driver, loac5).click()  # 选择单选
        # self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        self.driver.switch_to.parent_frame()
        loac6 = ("xpath", "//*[@class= 'ui-dialog-autofocus']")  # 确定按钮
        time.sleep(2)
        dengdai(self.driver, loac6).click()  # 点击确定按钮
        self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/SPF/cyqygl/ZZZSZXYY?bid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/SPF/cyqygl/ZZZSZXYY?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loactor = ("xpath", "//*[@class='dhtmlx_popup_text']")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "当前企业已有在办建档业务了！"))
        assert element4

