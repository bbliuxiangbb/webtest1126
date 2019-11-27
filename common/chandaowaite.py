#@Author: LIUXIANG
#@Time  :  2019/8/20 8:31

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
def dengdai(driver,loctor=("by","value"),timeout = 10,t = 0.5):
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element(*loctor))
    return  element

def is_text_in_element(self, loactor, _text):
    try:
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(loactor, _text))
        return result
    except:
        return False
# if  __name__ == "__main__":
#     from selenium import webdriver
#     driver = webdriver.Firefox()
#     driver.get("http://113.105.17.42:8080/zentao/my/")
#     loc1 = ("xpath", "//*[@id='account']")
#     loc2 = ("xpath", "//*[@name='password']")
#     loc3 = ("xpath", "//*[@id= 'submit']")
#     dengdai(driver, loc1).send_keys("lxx")
#     dengdai(driver, loc2).send_keys("lx5830..")
#     dengdai(driver, loc3).click()




