#@Author: LIUXIANG
#@Time  :  2019/8/19 12:36
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
def dengdai(driver ,loactor=("by","value"),timeout = 40,t = 0.5):
    # driver = webdriver.Firefox()
    element = WebDriverWait(driver, 240).until(lambda x: x.find_element(*loactor))
    return  element
def is_text_in_element(self, loactor, _text):
    try:
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(loactor, _text))
        return result
    except:
        return False

def is_element_on(self, loactor):
    try:
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.frame_to_be_available_and_switch_to_it(loactor))
        return result
    except:
        return False


 # def is_text_in_element(self, loactor, _text):
 #        try:
 #            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(loactor, _text))
 #            return result
 #        except:
 #            return False
# def text_to_be_present_in_element(loactor,_text):
#     element1element1 = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(loactor,"_text"))
# #     return element1
# if __name__ == "__main__":  #测试函数是否能用？
#     import time
#     from selenium import webdriver
#     from aip import AipOcr
#     from PIL import Image
#     from selenium.webdriver.support.ui import WebDriverWait
#     import os
#     from selenium import  webdriver
#     driver = webdriver.Firefox()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     driver.get(" http://113.105.17.42:8080/zentao/user-login.html")  # 地址栏里输入网址
#     loactor = ("xpath","//*[text()= '忘记密码']")
#     element2 = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(loactor, "忘记密码"))
#     print(element2)

    #
    # def is_text_in_element(self, loactor, _text):
    #     try:
    #         result = WebDriverWait(self.driver, self.timeout, self.t).until(
    #             EC.text_to_be_present_in_element(loactor, _text))
    #         return result
    #     except:
    #         return False
    #
    #
    # loc1 = ("xpath", "//*[@id='account']")
    # r1 = is_text_in_element(loc1, "用户名")
    # print(r1)
    # assert r1

    # ele1 =  WebDriverWait(driver, 30).until(lambda x: x.find_element("id","username")
    # ele1.send_keys("lx022002")
    # ele2 =  WebDriverWait(driver, 30).until(lambda x: x.find_element("class name","passwordbt")
    # ele2.send_keys("lx022002")
    # driver.find_element_by_id('username').send_keys("lx022002")  #
    # driver.find_element_by_class_name('passwordbt').send_keys("lx022002")
    # lac1 = ("id","username")
    # lac2 = ("class name","passwordbt")
    # dengdai(driver,lac1).send_keys("lx022002")
    # print(lac2)
    # dengdai(driver,lac2).send_keys("lx022002")
    # #
    # APP_ID = "16230456"
    # API_KEY = "8N2P8sUIB36F3imeui8tyflo"
    # SECRET_KEY = "9p291bmDeprXN3k6bgIBrShTIHEkVSDB "
    # client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # """ 读取图片 """
    #
    #
    # def get_file_content(filePath):
    #     with open(filePath, 'rb') as fp:
    #         return fp.read()
    #
    #
    # def getPic():
    #     # 获取截图
    #     driver.get_screenshot_as_file('screenshot.png')
    #     # 获取指定元素位置
    #     element = driver.find_element_by_xpath('//*[@id="yzm"]')
    #     print(element.size)
    #     print(element.location)
    #     # 获取位置不准，进行微调
    #     left = int(element.location['x'])
    #     top = int(element.location['y'])
    #     right = int(element.location['x'] + element.size['width'])
    #     bottom = int(element.location['y'] + element.size['height'])
    #     # 通过Image处理图像
    #     im = Image.open('screenshot.png')
    #     im = im.crop((left, top, right, bottom))
    #     im.save('code.png')
    #
    #
    # def getChar():
    #     getPic()
    #     image = get_file_content('code.png')
    #     """ 调用通用文字识别（高精度版） """
    #     result = client.basicAccurate(image)
    #     words_result = result.get("words_result")
    #     # 删除屏幕截图
    #     os.remove('screenshot.png')
    #     # 删除验证码截图
    #     os.remove('code.png')
    #     print(words_result)
    #     ss = words_result[0].get("words")
    #     # 删除空格
    #     ss = ss.replace(' ', '')
    #     return (ss)
    #
    #
    # driver.find_element_by_xpath('//*[@id="code"]').send_keys(getChar())  # 输入验证码
    # time.sleep(2)
    #
    # driver.find_element_by_xpath('//*[@onclick= "submitL();"]').click()  # 点登录
    # time.sleep(3)
    # a = driver.switch_to.alert
    #
    #
    # def is_alert_on():  # 定义一个判断是否有弹框的方法。
    #     try:
    #         t = a.text
    #         return True
    #     except:
    #         return False
    #
    #
    # while is_alert_on():  # 循环弹框出来了 。有弹框说明登录失败。
    #     a.accept()
    #     time.sleep(2)
    #     APP_ID = "16230456"
    #     API_KEY = "8N2P8sUIB36F3imeui8tyflo"
    #     SECRET_KEY = "9p291bmDeprXN3k6bgIBrShTIHEkVSDB "
    #     client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #     """ 读取图片 """
    #
    #
    #     def get_file_content(filePath):
    #         with open(filePath, 'rb') as fp:
    #             return fp.read()
    #
    #
    #     def getPic():
    #         # 获取截图
    #         driver.get_screenshot_as_file('screenshot.png')
    #         # 获取指定元素位置
    #         element = driver.find_element_by_xpath('//*[@id="yzm"]')
    #         print(element.size)
    #         print(element.location)
    #         # 获取位置不准，进行微调
    #         left = int(element.location['x'])
    #         top = int(element.location['y'])
    #         right = int(element.location['x'] + element.size['width'])
    #         bottom = int(element.location['y'] + element.size['height'])
    #         # 通过Image处理图像
    #         im = Image.open('screenshot.png')
    #         im = im.crop((left, top, right, bottom))
    #         im.save('code.png')
    #
    #
    #     def getChar():
    #         getPic()
    #         image = get_file_content('code.png')
    #         """ 调用通用文字识别（高精度版） """
    #         result = client.basicAccurate(image)
    #         words_result = result.get("words_result")
    #         # 删除屏幕截图
    #         os.remove('screenshot.png')
    #         # 删除验证码截图
    #         os.remove('code.png')
    #         print(words_result)
    #         ss = words_result[0].get("words")
    #         # 删除空格
    #         ss = ss.replace(' ', '')
    #         return (ss)
    #     driver.find_element_by_xpath('//*[@id="code"]').clear()
    #     time.sleep(1)
    #     driver.find_element_by_xpath('//*[@id="code"]').send_keys(getChar())
    #     time.sleep(3)
    #     lac3 = ("xpath","//*[@onclick= 'submitL();']")
    #     dengdai(driver,lac3).click()
    #     # ele3 = WebDriverWait(driver, 30).until(lambda x: x.find_element("xpath", "//*[@onclick= 'submitL();']")
    #     # ele3.click()
    #     # driver.find_element_by_xpath('//*[@onclick= "submitL();"]').click()  # 点登录
    #     time.sleep(3)
    # if is_alert_on():  # 如果弹框出来了，就点确定
    #     a.accept()
    #     time.sleep(5)
    # else:  # 否则就通过了
    #     pass

