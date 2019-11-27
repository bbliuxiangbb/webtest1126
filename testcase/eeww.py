#@Author: LIUXIANG
#@Time  :  2019/8/8 18:05
from selenium import webdriver
from aip import AipOcr
from PIL import Image
from selenium.webdriver.support.ui import Select
import os
import time
'''江门开发商入网职能端编辑修改人员信息，然后备案成功'''
driver = webdriver.Firefox()
# driver = webdriver.Ie()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(" http://168.168.28.17:8080/account/login")  # 地址栏里输入网址
driver.find_element_by_id('username').send_keys("lx022002")  #
driver.find_element_by_class_name('passwordbt').send_keys("lx022002")
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

driver.find_element_by_xpath('//*[@id="code"]').send_keys(getChar())
time.sleep(10)
driver.find_element_by_xpath('//*[@onclick= "submitL();"]').click()  # 点登录
time.sleep(10)
driver.find_element_by_xpath("//*[text()='从业主体管理']").click()
time.sleep(5)
driver.find_element_by_id("9a19f838-6794-47ba-97c1-b5645e372aea企业申请查询").click()
time.sleep(15)
driver.switch_to.default_content()
# a = driver.find_element_by_xpath("//*[@id='index']/div[4]/div[2]/div[2]/div/div/div/div[3]/div/iframe")  #2种方式都可以
a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'../BusinessHandle/ModuleChooicer?fid=')]")
driver.switch_to.frame(a)
driver.find_element_by_xpath("//*[@id= 'seach_Columname']/option[3]").click()
driver.find_element_by_id('seach_Text').send_keys("江门明明大有限公司")  # 输入企业名称
driver.find_element_by_id('Btn_Seach').click()
time.sleep(5)
# driver.find_element_by_id('icon-legal bigger-130').click()
time.sleep(3)
# driver.find_element_by_xpath("//*[@class= 'icon-legal bigger-130']").click()  # 点受理 待受理
driver.find_element_by_xpath("//*[@class= 'icon-eye-open bigger-130']").click()  # 受理中 第二次
time.sleep(15)
driver.switch_to.default_content()
a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/BusinessHandle/ModuleChooicer?bid=')]")  # 备案按钮受理界面iframe
driver.switch_to.frame(a)
time.sleep(2)
driver.find_element_by_xpath("//*[@id = 'QYMC']").send_keys("3232")
# driver.find_element_by_link_text("从业人员").click()
# driver.find_element_by_xpath("//*[text()='从业人员']").click()

# driver.find_element_by_xpath("//*[text()='资质信息']").click()      //*[@id='myTab']/li[4]/a
driver.find_element_by_xpath("//*[@id='myTab']/li[4]/a").click()
time.sleep(6)
driver.switch_to_frame("iframeqyry")
driver.find_element_by_xpath("//*[@id='tb_cyry']/tr[1]/td[1]/label/input").click()
driver.find_element_by_xpath("//*[@id = 'btnEditCYRY']").click()
time.sleep(3)
a= driver.find_element_by_xpath("//iframe[starts-with(@src, '/InternalDialog/CYRY.aspx?bid=')]")
driver.switch_to_frame(a)
driver.find_element_by_xpath('//*[@id="XM"]').send_keys("邹空间")