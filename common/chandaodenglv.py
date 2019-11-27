#@Author: LIUXIANG
#@Time  :  2019/8/23 20:26
from selenium import  webdriver
from aip import  AipOcr
import  os
import time
from PIL import  Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
def chaodaodv(driver,user = "lxx", psw = "lx5830.."):
    driver.get("http://113.105.17.42:8080/zentao/user-login.html")
    driver.find_element_by_xpath("//*[@id = 'account']").send_keys(user)
    driver.find_element_by_xpath("//*[@name= 'password']").send_keys(psw)
    driver.find_element_by_xpath("//*[@id = 'submit']").click()
# if  __name__ == "__main__":
#     from selenium import webdriver
#     driver = webdriver.Firefox()
#     chaodaodv(driver)
#     time.sleep(3)
#     driver.find_element_by_link_text("测试").click()
#     # t = driver.find_element_by_xpath("//*[@class = 'icon-user']").text
#
#     time.sleep(3)
#     driver.find_element_by_link_text("组织").click()





