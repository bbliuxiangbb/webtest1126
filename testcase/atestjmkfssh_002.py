# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()

from selenium import webdriver
from aip import AipOcr
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
from  common.login import loginxt
import unittest
class JmrwshTest(unittest.TestCase):
    '''江门开发商入网正常审核'''
    def test_11(self):
        '''江门开发商入网正常审核成功'''
        driver = webdriver.Firefox()
        loginxt(driver,"lx022002","lx022002")
        # # driver = webdriver.Ie()
        # driver.implicitly_wait(10)
        # driver.maximize_window()
        # # a = "广州金山1开发有限公司"  # 企业名称
        # driver.get("http://168.168.28.17:8080/account/login")  # 地址栏里输入网址
        # driver.find_element_by_id('username').send_keys("lx022002")  #
        # driver.find_element_by_class_name('passwordbt').send_keys("lx022002")
        # APP_ID = "16230456"
        # API_KEY = "8N2P8sUIB36F3imeui8tyflo"
        # SECRET_KEY = "9p291bmDeprXN3k6bgIBrShTIHEkVSDB "
        # client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        # """ 读取图片 """
        # def get_file_content(filePath):
        #     with open(filePath, 'rb') as fp:
        #         return fp.read()
        # def getPic():
        #     #获取截图
        #     driver.get_screenshot_as_file('screenshot.png')
        #     #获取指定元素位置
        #     element = driver.find_element_by_xpath('//*[@id="yzm"]')
        #     print(element.size)
        #     print(element.location)
        #     #获取位置不准，进行微调
        #     left = int(element.location['x'])
        #     top = int(element.location['y'])
        #     right = int(element.location['x'] + element.size['width'])
        #     bottom = int(element.location['y'] + element.size['height'])
        #     #通过Image处理图像
        #     im = Image.open('screenshot.png')
        #     im = im.crop((left, top, right, bottom))
        #     im.save('code.png')
        # def getChar():
        #     getPic()
        #     image = get_file_content('code.png')
        #     """ 调用通用文字识别（高精度版） """
        #     result = client.basicAccurate(image)
        #     words_result = result.get("words_result")
        #     #删除屏幕截图
        #     os.remove('screenshot.png')
        #     #删除验证码截图
        #     os.remove('code.png')
        #     print(words_result)
        #     ss = words_result[0].get("words")
        #     #删除空格
        #     ss = ss.replace(' ','')
        #     return(ss)
        # driver.find_element_by_xpath('//*[@id="code"]').send_keys(getChar())
        # time.sleep(8)
        # driver.find_element_by_xpath('//*[@onclick= "submitL();"]').click() #点登录
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
        driver.find_element_by_id('seach_Text').send_keys("江门明明空楼有限公司")  # 输入企业名称
        driver.find_element_by_id('Btn_Seach').click()
        time.sleep(5)
        # driver.find_element_by_id('icon-legal bigger-130').click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@class= 'icon-legal bigger-130']").click()  #点受理 待受理
        # driver.find_element_by_xpath("//*[@class= 'icon-eye-open bigger-130']").click()  # 受理中 第二次
        time.sleep(15)
        driver.switch_to.default_content()
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/BusinessHandle/ModuleChooicer?bid=')]")#  备案按钮终审中界面iframe
        driver.switch_to.frame(a)
        time.sleep(2)
        driver.find_element_by_id("TopButtons_btnRecord").click() #点备案
        time.sleep(10)
        driver.switch_to.default_content()
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/Common/SPYJGL.aspx?bid=')]")# 填写意见iframe
        driver.switch_to.frame(a)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='txtspyj']").send_keys("20190730shenhe")  #填写意见
        driver.switch_to.parent_frame()# 回到上一层iframe
        time.sleep(2)
        driver.find_element_by_xpath("//*[text()='确定']").click()  #点确定
        time.sleep(25)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[text()='确定']").click()  #点确定
        time.sleep(5)
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/BusinessHandle/ModuleChooicer?bid=')]")  # 缮证iframe
        driver.switch_to.frame(a)
        time.sleep(5)
        driver.find_element_by_id("TopButtons_btnSZ").click() #点缮证
        time.sleep(25)
        driver.switch_to.default_content()
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'../SPF/Cyqygl/JMZZSZ?bid=')]")  #缮证里面信息iframe
        driver.switch_to.frame(a)
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//*[text()='生成']").click()  #点生成
        driver.find_element_by_id("FZJG").send_keys("不动产登记中心")
        driver.find_element_by_id("SCFZSJ").send_keys("2019-07-29")
        driver.find_element_by_id("YXQSRQ").send_keys("2019-07-29")
        driver.find_element_by_id("YXJSRQ").send_keys("2022-07-29")
        driver.find_element_by_id("BZ").send_keys("20190729备注资质信息")
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath("//*[text()='确定']").click() #点确定缮证成功
        time.sleep(15)
        driver.switch_to.default_content()
        time.sleep(8)
        driver.find_element_by_xpath("//*[text()='确定']").click() #点确定
        time.sleep(10)
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/BusinessHandle/ModuleChooicer?bid=')]")  #电脑归档iframe
        driver.switch_to.frame(a)
        time.sleep(5)
        driver.find_element_by_id("TopButtons_btnDNGD").click() #点电脑归档
        time.sleep(8)
        driver.switch_to.default_content()
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'../JYBA/Fwsyqzyba/Spf_Ljgd?bid=')]")
        driver.switch_to.frame(a)
        driver.implicitly_wait(3)
        a = driver.find_element_by_xpath("//*[@id='dt_tbody']/tr[1]/td[4]/input").send_keys("1")
        a = driver.find_element_by_xpath("//*[@id='dt_tbody']/tr[1]/td[5]/input").send_keys("1")
        a = driver.find_element_by_xpath("//*[@id='dt_tbody']/tr[2]/td[4]/input").send_keys("1")
        a = driver.find_element_by_xpath("//*[@id='dt_tbody']/tr[2]/td[5]/input").send_keys("1")
        a = driver.find_element_by_xpath("//*[@id='dt_tbody']/tr[3]/td[4]/input").send_keys("1")
        a = driver.find_element_by_xpath("//*[@id='dt_tbody']/tr[3]/td[5]/input").send_keys("1")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@class = 'dhxtoolbar_text'and text()= '保存'] ").click() #保存
        time.sleep(4)
        driver.switch_to.default_content()
        time.sleep(2)
        driver.find_element_by_xpath("//*[text()='确定']").click()
        time.sleep(3)
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'../JYBA/Fwsyqzyba/Spf_Ljgd?bid=')]")
        driver.switch_to.frame(a)
        driver.find_element_by_xpath("//*[@class = 'dhxtoolbar_text'and text()= '关闭'] ").click()#关闭
        time.sleep(2)
        driver.switch_to.default_content()
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/BusinessHandle/ModuleChooicer?bid=')]")
        driver.switch_to.frame(a)
        time.sleep(5)
        driver.find_element_by_id("TopButtons_btnSubmit").click() #点提交
        time.sleep(5)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[text()='确定']").click()
        time.sleep(5)
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/BusinessHandle/ModuleChooicer?bid=')]")  #实物件归档iframe
        driver.switch_to.frame(a)
        time.sleep(2)
        driver.find_element_by_id("TopButtons_btnSWJGD").click() #点实物件归档
        time.sleep(8)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[text()='确定']").click()
        time.sleep(3)
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/BusinessHandle/ModuleChooicer?bid=')]")  # 已办结iframe
        driver.switch_to.frame(a)
        t= driver.find_element_by_xpath("//*[@id='btnPrint']/button").text  #获取到打印按钮说明提交成功了
        # print(t)
        self.assertTrue(t=='打印')
        driver.close()
        # t = driver.find_element_by_xpath("//*[@class = 'tdTitleText fright'and text()= '入网状态：']").text
        # print(t)
        # self.assertTrue(t =='有效')

    def test_12(self):
        '''江门开发商入网职能端退件成功'''
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
        driver.find_element_by_id('seach_Text').send_keys("江门明明小有限公司")  # 输入企业名称
        driver.find_element_by_id('Btn_Seach').click()
        time.sleep(5)
        # driver.find_element_by_id('icon-legal bigger-130').click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@class= 'icon-legal bigger-130']").click()  # 点受理 待受理
        # driver.find_element_by_xpath("//*[@class= 'icon-eye-open bigger-130']").click()  # 受理中 第二次
        time.sleep(15)
        driver.switch_to.default_content()
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/BusinessHandle/ModuleChooicer?bid=')]")  # 备案按钮受理界面iframe
        driver.switch_to.frame(a)
        time.sleep(2)
        driver.find_element_by_id("TopButtons_btnReturn").click()  # 点退件
        time.sleep(10)
        driver.switch_to.default_content()
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/Common/SPYJGL.aspx?bid=')]")  # 填写意见iframe
        driver.switch_to.frame(a)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='txtspyj']").send_keys("同意退件")  # 填写意见
        driver.switch_to.parent_frame()  # 回到上一层iframe
        time.sleep(2)
        driver.find_element_by_xpath("//*[text()='确定']").click()  # 点确定
        time.sleep(15)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[text()='确定']").click()  # 点确定
        time.sleep(4)
        # t= driver.find_element_by_xpath("//*[@data-toggle='dropdown'and @onclick= ' return false;']").text
        # print(t)
        # self.assertFalse(t =='打印')
        a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/BusinessHandle/ModuleChooicer?bid=')]")  # 已办结iframe
        driver.switch_to.frame(a)
        t = driver.find_element_by_xpath("//*[@class = 'watermark']").text
        print(t)
        self.assertTrue(t== '')
        driver.close()

    # def test_13(self):
    #     '''江门开发商入网职能端编辑修改人员信息，然后备案成功'''
    #     driver = webdriver.Firefox()
    #     # driver = webdriver.Ie()
    #     driver.implicitly_wait(10)
    #     driver.maximize_window()
    #     driver.get(" http://168.168.28.17:8080/account/login")  # 地址栏里输入网址
    #     driver.find_element_by_id('username').send_keys("lx022002")  #
    #     driver.find_element_by_class_name('passwordbt').send_keys("lx022002")
    #     time.sleep(2)
    #     APP_ID = "16230456"
    #     API_KEY = "8N2P8sUIB36F3imeui8tyflo"
    #     SECRET_KEY = "9p291bmDeprXN3k6bgIBrShTIHEkVSDB "
    #     client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #     """ 读取图片 """
    #
    #     def get_file_content(filePath):
    #         with open(filePath, 'rb') as fp:
    #             return fp.read()
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
    #
    #         # 通过Image处理图像
    #         im = Image.open('screenshot.png')
    #         im = im.crop((left, top, right, bottom))
    #         im.save('code.png')
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
    #
    #     driver.find_element_by_xpath('//*[@id="code"]').send_keys(getChar())
    #     time.sleep(10)
    #     driver.find_element_by_xpath('//*[@onclick= "submitL();"]').click()  # 点登录
    #     time.sleep(10)
    #     driver.find_element_by_xpath("//*[text()='从业主体管理']").click()
    #     time.sleep(5)
    #     driver.find_element_by_id("9a19f838-6794-47ba-97c1-b5645e372aea企业申请查询").click()
    #     time.sleep(15)
    #     driver.switch_to.default_content()
    #     # a = driver.find_element_by_xpath("//*[@id='index']/div[4]/div[2]/div[2]/div/div/div/div[3]/div/iframe")  #2种方式都可以
    #     a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'../BusinessHandle/ModuleChooicer?fid=')]")
    #     driver.switch_to.frame(a)
    #     driver.find_element_by_xpath("//*[@id= 'seach_Columname']/option[3]").click()
    #     driver.find_element_by_id('seach_Text').send_keys("江门明明大有限公司")  # 输入企业名称
    #     driver.find_element_by_id('Btn_Seach').click()
    #     time.sleep(5)
    #     # driver.find_element_by_id('icon-legal bigger-130').click()
    #     time.sleep(3)
    #     # driver.find_element_by_xpath("//*[@class= 'icon-legal bigger-130']").click()  # 点受理 待受理
    #     driver.find_element_by_xpath("//*[@class= 'icon-eye-open bigger-130']").click()  # 受理中 第二次
    #     time.sleep(15)
    #     driver.switch_to.default_content()
    #     a = driver.find_element_by_xpath("//iframe[starts-with(@src ,'/BusinessHandle/ModuleChooicer?bid=')]")  # 备案按钮受理界面iframe
    #     driver.switch_to.frame(a)
    #     time.sleep(2)
    #     # driver.find_element_by_link_text("从业人员").click()
    #     driver.find_element_by_xpath("//*[text()='从业人员']").click()
    #     time.sleep(6)
    #     driver.switch_to_frame("iframeqyry")
    #     driver.find_element_by_xpath("//*[@id='tb_cyry']/tr[1]/td[1]/label/input").click()
    #     driver.find_element_by_xpath("//*[@id = 'btnEditCYRY']").click()
    #     time.sleep(3)
    #     a= driver.find_element_by_xpath("//iframe[starts-with(@src, '/InternalDialog/CYRY.aspx?bid=')]")
    #     driver.switch_to_frame(a)
    #     driver.find_element_by_xpath('//*[@id="XM"]').send_keys("邹空间")
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
    #         #
    #         # driver.find_element_by_id("TopButtons_btnReturn").click()  # 点退件
    #         # time.sleep(10)
    #         # driver.switch_to.default_content()
