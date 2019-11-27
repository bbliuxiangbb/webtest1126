#@Author: LIUXIANG
#@Time  :  2019/8/24 13:52

from selenium import  webdriver
from aip import  AipOcr
import  os
import time
from PIL import  Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
def loginxt2(driver, user="lx022002" ,name="lx022002" ):
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(" http://168.168.28.17:8080/Account/Login")  # 地址栏里输入网址
    driver.find_element_by_id('username').send_keys(user)  #
    driver.find_element_by_class_name('passwordbt').send_keys(name)
    APP_ID = "17076224"
    API_KEY = "cnoCyIpYmP4bORTQ9k8zYwno"
    SECRET_KEY = "1AGS8rD9ZvVcwPq8rQeRz9IbuuRpHGhx"
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    def getPic():
        # 获取截图
        driver.get_screenshot_as_file('screenshot.png')
        # 获取指定元素位置
        element = driver.find_element_by_xpath('//*[@id="yzm"]')
        print(element.size)
        print(element.location)
        # 获取位置不准，进行微调
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = int(element.location['x'] + element.size['width'])
        bottom = int(element.location['y'] + element.size['height'])
        # 通过Image处理图像
        im = Image.open('screenshot.png')
        im = im.crop((left, top, right, bottom))
        im.save('code.png')
    def getChar():
        getPic()
        image = get_file_content('code.png')
        """ 调用通用文字识别（高精度版） """
        result = client.basicAccurate(image)
        words_result = result.get("words_result")
        # 删除屏幕截图
        os.remove('screenshot.png')
        # 删除验证码截图
        os.remove('code.png')
        print(words_result)
        ss = words_result[0].get("words")
        # 删除空格
        ss = ss.replace(' ', '')
        return (ss)
    driver.find_element_by_xpath('//*[@id="code"]').send_keys(getChar())  # 输入验证码
    time.sleep(2)
    driver.find_element_by_xpath('//*[@onclick= "submitL();"]').click()  # 点登录
    time.sleep(3)
    a = driver.switch_to.alert
    def is_alert_on():  # 定义一个判断是否有弹框的方法。
        try:
            t = a.text
            return True
        except:
            return False

    while is_alert_on():  # 循环弹框出来了 。有弹框说明登录失败。
        a.accept()
        time.sleep(2)
        APP_ID = "16230456"
        API_KEY = "8N2P8sUIB36F3imeui8tyflo"
        SECRET_KEY = "9p291bmDeprXN3k6bgIBrShTIHEkVSDB "
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        """ 读取图片 """

        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()

        def getPic():
            # 获取截图
            driver.get_screenshot_as_file('screenshot.png')
            # 获取指定元素位置
            element = driver.find_element_by_xpath('//*[@id="yzm"]')
            print(element.size)
            print(element.location)
            # 获取位置不准，进行微调
            left = int(element.location['x'])
            top = int(element.location['y'])
            right = int(element.location['x'] + element.size['width'])
            bottom = int(element.location['y'] + element.size['height'])
            # 通过Image处理图像
            im = Image.open('screenshot.png')
            im = im.crop((left, top, right, bottom))
            im.save('code.png')

        def getChar():
            getPic()
            image = get_file_content('code.png')
            """ 调用通用文字识别（高精度版） """
            result = client.basicAccurate(image)
            words_result = result.get("words_result")
            # 删除屏幕截图
            os.remove('screenshot.png')
            # 删除验证码截图
            os.remove('code.png')
            print(words_result)
            ss = words_result[0].get("words")
            # 删除空格
            ss = ss.replace(' ', '')
            return (ss)

        driver.find_element_by_xpath('//*[@id="code"]').clear()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="code"]').send_keys(getChar())
        time.sleep(3)
        driver.find_element_by_xpath('//*[@onclick= "submitL();"]').click()  # 点登录
        time.sleep(3)
    if is_alert_on():  # 如果弹框出来了，就点确定
        a.accept()
        time.sleep(5)
    else:  # 否则就通过了
        pass
# if __name__ =="__main__":
#
#     driver= webdriver.Firefox()
#     loginxt2(driver)