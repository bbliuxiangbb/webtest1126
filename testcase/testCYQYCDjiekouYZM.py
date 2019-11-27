#@Author: LIUXIANG
#@Time  :  2019/8/21 8:16    ${DATE} ${TIME}
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
class CYyqyJiekou(unittest.TestCase):
    '''职能端从业主体系统各菜单查询，引用，调档功能测试'''
    # @classmethod  #类方法
    # def setUpClass(cls) -> None:
    #     cls.driver = webdriver.Firefox()
    #     loginxt(cls.driver, "lx022002", "lx022002")
        # self.login_page = LoginPage(self.driver)
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        loginxt(self.driver, "lx022002", "lx022002")
        loc1 = ("xpath", "//*[text()='从业主体管理']")
        dengdai(self.driver, loc1).click()
    def tearDown(self) -> None:
        self.driver.close()
    def testcyqy_01(self):
        '''从业主体管理，企业备案_开发商企业菜单查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'da89c334-7f86-4625-8573-9751c3a94984企业备案_开发商企业']")
        dengdai(self.driver, loc2).click()
        # a=self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]") #切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3= ("xpath","//*[@id = 'Btn_Seach']")
        dengdai(self.driver,loc3).click()  #点查询
        time.sleep(3)
        loactor = ("xpath","//*[@class='first disabled']/a")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "首页"))
        assert element1  #断言能不能获取 首页
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_02(self):
        '''从业主体管理，企业备案_其他企业查询功能'''
        # self.driver = webdriver.Firefox()
        # loginxt(self.driver, "lx022002", "lx022002")
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(self.driver, loc1).click()
        # self.driver.switch_to.default_content()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '88a4ad1c-331c-45f5-a07b-96c3f2196e1a企业备案_其他企业']")
        dengdai(self.driver, loc2).click()
        # a=self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(3)
        loactor = ("xpath","//*[@id='QybaList']/thead/tr/th[1]")
        element2 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "网上申请号"))
        assert element2
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_03(self):
        '''从业主体管理，从业人员管理查询功能'''
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '301e73fd-3b66-4f80-9c30-8ddf8151587d从业人员管理']")
        dengdai(self.driver, loc2).click()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@id='RyglList']/thead/tr/th[5]")
        element3 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "职称证书编号"))
        assert element3
        # self.driver.switch_to.default_content()
        # self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_04(self):
        '''从业主体管理，从业企业管理查询功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '4b381016-bb1e-43ac-aa56-284077e5ba05从业企业管理']")
        dengdai(self.driver, loc2).click()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@id='QybaList']/thead/tr/th[3]")
        element3 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "企业类型"))
        assert element3
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
        # t = driver.find_element_by_xpath("//*[@id='RyglList']/thead/tr/th[5]").text
        # print(t)
    def testcyqy_05(self):
        '''从业主体管理，企业申请查询功能'''
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '9a19f838-6794-47ba-97c1-b5645e372aea企业申请查询']")
        dengdai(self.driver, loc2).click()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@id='RyglList']/thead/tr/th[5]")
        element3 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "网上申请号"))
        assert element3
        # self.driver.switch_to.default_content()
        # self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    #     # t = driver.find_element_by_xpath("//*[@id='RyglList']/thead/tr/th[5]").text
    def testcyqy_06(self):
        '''从业主体管理，企业变更菜单引用企业功能'''
        # time.sleep(2)
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '3932fc1e-c9a3-4186-ba0a-c7b3c6cdb546企业信息变更']")
        dengdai(self.driver, loc2).click()# 点企业信息变更菜单
        time.sleep(5)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 200).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@id = 'TopButtons_btnQYApply']")  #引用按钮
        dengdai(self.driver, loac3).click()  # 点引用按钮
        self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/Common/YYQYJBXX.aspx?bid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/Common/YYQYJBXX.aspx?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac4 = ("xpath", "//*[@id = 'btnSearch']")  # 查询按钮
        time.sleep(2)
        dengdai(self.driver, loac4).click()
        loac5 = ("name","checkRadio")
        dengdai(self.driver, loac5).click()
        loac6 = ("xpath", "//*[@id = 'btnYYQYXX']")  # 确定引用按钮
        time.sleep(3)
        dengdai(self.driver, loac6).click() #点击确定引用按钮
        time.sleep(3)
        self.driver.switch_to.default_content() #回到默认顶层
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        time.sleep(1)
        # 方法1
        # t= driver.find_element_by_xpath("//*[@class = 'widget-header widget-header-small']").text
        # # print(t)#业务受理信息
        # assert t
        #方法2
        loactor = ("xpath", "//*[@class = 'widget-header widget-header-small']")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "业务受理信息"))
        assert element4
        # self.driver.switch_to.default_content()
        # self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()

    def testcyqy_07(self):
        '''从业主体管理，业务查询菜单查询功能'''
        # driver = webdriver.Firefox()
        # loginxt2(driver, "lx022002", "lx022002")
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'b68cbc57-9ec9-4488-8a6b-a8feecccdfd6业务查询']")
        dengdai(self.driver, loc2).click()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        time.sleep(3)
        loactor = ("xpath", "//*[@class='first disabled']/a")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "首页"))
        assert element1  # 断言能不能获取 首页
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_08(self):
        '''从业主体管理，从业账号管理菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = 'e76aa68f-6f21-4be3-b810-72f5059d6fa1从业账号管理']")
        dengdai(self.driver, loc2).click()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'cxan']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 首页
        # self.driver.switch_to.default_content()
        # self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_09(self):
        '''从业主体管理，企业备案_经纪机构菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '398b72d7-7e93-4362-a5d0-d72042ed96a8企业备案_经纪机构']")
        dengdai(self.driver, loc2).click()
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class='first disabled']/a")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "首页"))
        assert element1  # 断言能不能获取 首页
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_10(self):
        '''从业主体管理，企业注销_经纪机构菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '09ffcdd5-54eb-46c6-9489-4004ec0d5f1e企业注销_经纪机构']")
        dengdai(self.driver, loc2).click()
        # time.sleep(2)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class='first disabled']/a")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "首页"))
        assert element1  # 断言能不能获取 首页
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_11(self):
        '''从业主体管理，企业备案_物业企业菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '78b4a65f-aaf4-4da5-8210-36f2f8b429bc企业备案_物业企业']")
        dengdai(self.driver, loc2).click()
        # a = self.driver.find_element_by_xpath( "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class='first disabled']/a")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "首页"))
        assert element1  # 断言能不能获取 首页
        # self.driver.switch_to.default_content()
        # self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_12(self):
        '''从业主体管理，待办业务菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '8a863cf7-a35e-4658-9060-a0ce3953644c待办业务']")
        dengdai(self.driver, loc2).click()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
        # self.driver.switch_to.default_content()
        # self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_13(self):
        '''从业主体管理，已办业务菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '1677e3ba-332f-4808-98ad-d51c14b3e501已办业务']")
        dengdai(self.driver, loc2).click()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'btnSearch']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class ='dhxtoolbar_text'and text()= '跳页']")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))
        assert element1  # 断言能不能获取 跳页
        self.driver.switch_to.default_content()
        # self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_14(self):
        '''从业主体管理，企业年审审批菜单引用企业功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '379b4f6c-78fc-41c1-ab8a-0309f5b35b1b企业年审审批']")
        dengdai(self.driver, loc2).click()  # 点企业信息年审菜单
        time.sleep(4)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@id = 'TopButtons_btnQYApply']")  # 引用按钮
        dengdai(self.driver, loac3).click()  # 点引用按钮
        time.sleep(5)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/SPF/Cyqygl/NSSP_YYQY?bid')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/SPF/Cyqygl/NSSP_YYQY?bid')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac4 = ("xpath", "//*[@id = 'btnSearch']")  # 查询按钮
        dengdai(self.driver, loac4).click()
        loac5 = ("name", "checkRadio")
        dengdai(self.driver, loac5).click()
        loac6 = ("xpath", "//*[@id = 'btnYYQYXX']")  # 确定引用按钮
        dengdai(self.driver, loac6).click()  # 点击确定引用按钮
        time.sleep(8)
        self.driver.switch_to.default_content()  # 回到默认顶层
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        self.driver.switch_to.frame("iframesqxx")
        time.sleep(3)
        # 方法2
        # loactor= driver.find_element_by_xpath("//*[@id='applicantMassage']/div/div[1]/div[1]").text
        # print(loactor)
        loactor = ("xpath", "//*[@id='applicantMassage']/div/div[1]/div[1]")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "企业名称："))
        assert element4
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_15(self):
        '''从业主体管理，企业备案_安全鉴定机构菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(driver, loc1).click()
        time.sleep(2)
        loc2 = ("xpath", "//*[@id = '969a58f9-9747-41e2-96dc-e698cca5b569企业备案_安全鉴定机构']")
        dengdai(self.driver, loc2).click()
        # a = self.driver.find_element_by_xpath( "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        # dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class='first disabled']/a")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "首页"))
        assert element1  # 断言能不能获取 首页
        # self.driver.switch_to.default_content()
        # self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_16(self):
        '''从业主体管理，鉴定机构企业管理菜单查询功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '02474269-35f8-41e6-85f9-a987115dd8c5鉴定机构企业管理']")
        dengdai(self.driver, loc2).click()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loc3 = ("xpath", "//*[@id = 'Btn_Seach']")
        dengdai(self.driver, loc3).click()  # 点查询
        loactor = ("xpath", "//*[@class='first disabled']/a")
        element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "首页"))
        assert element1  # 断言能不能获取 首页
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_17(self):
        '''从业主体管理，企业资质证书注销申请受理菜单引用企业功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '666097ca-adc4-4945-8e68-2cc06772cd4d企业资质证书注销申请受理']")
        dengdai(self.driver, loc2).click()  # 点企业信息年审菜单
        time.sleep(4)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
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
        loac4 = ("xpath", "//*[@id = 'btnSearch']")  # 查询按钮
        dengdai(self.driver, loac4).click()
        loac5 = ("name", "QYID")
        dengdai(self.driver, loac5).click()  #选择单选
        self.driver.switch_to.default_content()
        loac6 = ("xpath", "//*[@class = 'ui-dialog-autofocus']")  # 确定按钮
        time.sleep(2)
        dengdai(self.driver, loac6).click()  # 点击确定按钮
        self.driver.switch_to.default_content()  # 回到默认顶层
        time.sleep(2)
        a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        self.driver.switch_to.frame(a)
        # 方法2
        # loactor= driver.find_element_by_xpath("//*[@id='tableForm']/div[1]/div/div/div[1]").text
        # print(loactor)
        loactor = ("xpath", "//*[@id='tableForm']/div[1]/div/div/div[1]")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "业务受理信息"))
        assert element4
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@class= 'dhxtabbar_tab_close']").click()
    def testcyqy_18(self):
        '''从业主体管理，企业资质证书补录菜单引用企业功能'''
        # loc1 = ("xpath", "//*[text()='从业主体管理']")
        # dengdai(self.driver, loc1).click()
        time.sleep(1)
        loc2 = ("xpath", "//*[@id = '5e4cf7cb-1309-4578-af64-f4452f7eca67企业资质证书补录']")
        dengdai(self.driver, loc2).click()  # 点企业信息年审菜单
        time.sleep(4)
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac3 = ("xpath", "//*[@id = 'btnCite']")  # 引用按钮
        dengdai(self.driver, loac3).click()  # 点引用按钮
        # time.sleep(3)
        self.driver.switch_to.default_content()
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'/SPF/cyqygl/ZZZSZXYY?bid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'/SPF/cyqygl/ZZZSZXYY?bid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        loac4 = ("xpath", "//*[@id = 'btnSearch']")  # 查询按钮
        dengdai(self.driver, loac4).click()
        loac5 = ("name", "QYID")
        dengdai(self.driver, loac5).click()  # 选择单选
        self.driver.switch_to.default_content()
        loac6 = ("xpath", "//*[@class = 'ui-dialog-autofocus']")  # 确定按钮
        time.sleep(2)
        dengdai(self.driver, loac6).click()  # 点击确定按钮
        time.sleep(1)
        self.driver.switch_to.default_content()  # 回到默认顶层
        # a = self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")
        # self.driver.switch_to.frame(a)
        loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
        WebDriverWait(self.driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        # 方法2
        # loactor= driver.find_element_by_xpath("//*[@id='tableForm']/div[1]/div/div/div[1]").text
        # print(loactor)
        loactor = ("xpath", "//*[@class='trTitleText']")
        element4 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "基本信息"))
        assert element4

    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #     # loactor = ("xpath", "//*[@id='btnSearch']")
    #     # element3 = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(loactor, "网上申请号"))
    #     # assert element3
    #     # # t = driver.find_element_by_xpath("//*[@id='RyglList']/thead/tr/th[5]").text
    #     # # print(t)
    #     # driver.close()