#@Author: LIUXIANG
#@Time  :  2019/10/8 9:48
from selenium import webdriver
from aip import AipOcr
import os
import time
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Base():
    '''基于原生的selenium做二次封装'''
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 30
        self.t = 0.5
    def findElement(self,loctor):
        element = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*loctor))
        return  element






class Login():
   def loginxt(self,driver, user="lx022002", name="lx022002"):
        # driver = webdriver.Firefox()
        # driver = webdriver.Ie()
        driver.maximize_window()
        driver.get(" http://168.168.28.17:8080/Account/Login")  # 地址栏里输入网址
        # driver.get("http://192.168.68.216/Account/Login")
        driver.find_element_by_id('username').send_keys(user)  #
        driver.find_element_by_class_name('passwordbt').send_keys(name)
        driver.find_element_by_xpath('//*[@onclick= "submitL();"]').click()  # 点登录
        time.sleep(3)