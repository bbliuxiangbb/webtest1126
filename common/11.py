#@Author: LIUXIANG
#@Time  :  2019/9/9 8:56
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from aip import AipOcr
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.login import loginxt
from common.webwa import dengdai
def get_huoqu_tiaoye(self):
    loactor = ("xpath", "//*[@id='cxlb_pagingArea']/div/div[9]")
    element1 = WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(loactor, "跳页"))

if __name__ == "__main__":
    time.sleep(2)
    driver = webdriver.Firefox()
    loginxt(driver, "lx022002", "lx022002")
    loc1 = ("xpath", "//*[text()='公告管理']")
    dengdai(driver, loc1).click()
    # time.sleep(3)
    # self.driver.find_element_by_xpath("//*[text()='公告管理']").click()
    loc2 = ("xpath", "//*[@id = '1318d068-196c-4af8-b6d9-939a30e1eeee公告管理']")
    dengdai(driver, loc2).click()
    loactor = ("xpath", "//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]")  # 切换iframe
    WebDriverWait(driver, 100).until(EC.frame_to_be_available_and_switch_to_it(loactor))
    # time.sleep(3)
    # a=self.driver.find_element_by_xpath("//iframe[starts-with(@src,'../BusinessHandle/ModuleChooicer?fid=')]") #切换iframe
    # self.driver.switch_to.frame(a)
    loc3 = ("xpath", "//*[@onclick= 'searchClick();']")
    dengdai(driver, loc3).click()  # 点查询

