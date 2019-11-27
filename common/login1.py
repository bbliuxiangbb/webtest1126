#@Author: LIUXIANG
#@Time  :  2019/8/24 13:38

from selenium import  webdriver
from aip import  AipOcr
import  os
import time
from PIL import  Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
def loginxt1(driver, user="lx022002" ,name="lx022002" ):
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(" http://168.168.28.17:8080/Account/Login")  # 地址栏里输入网址
    driver.find_element_by_id('username').send_keys(user)  #
    driver.find_element_by_class_name('passwordbt').send_keys(name)
    driver.find_element_by_xpath('//*[@onclick= "submitL();"]').click()  # 点登录
    time.sleep(3)
if __name__ =="__main__":

    driver= webdriver.Firefox()
    loginxt1(driver)