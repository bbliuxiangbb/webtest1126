#@Author: LIUXIANG
#@Time  :  2019/8/14 11:10
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from aip import AipOcr
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
import os
from common.login import loginxt
import unittest
class LoginTest(unittest.TestCase):
    '''正常网签商品房签合同成功'''
    def test_ht_01(self):
        driver = webdriver.Firefox()
        loginxt(driver,"td002","td002A")
        # driver.implicitly_wait(10)
        # driver.maximize_window()
        # driver.get("http://168.168.28.17:8080/Account/Login")  # 地址栏里输入网址
        # driver.find_element_by_id('username').send_keys("td002")  # 输入用户名
        # driver.find_element_by_class_name('passwordbt').send_keys("td002A")  # 输入密码
        # # 调取百度接口识别验证码
        # APP_ID = "16230456"
        # API_KEY = "8N2P8sUIB36F3imeui8tyflo"
        # SECRET_KEY = "9p291bmDeprXN3k6bgIBrShTIHEkVSDB "
        # client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        # """ 读取图片 """
        # def get_file_content(filePath):
        #     with open(filePath, 'rb') as fp:
        #         return fp.read()
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
        #
        #     # 通过Image处理图像
        #     im = Image.open('screenshot.png')
        #     im = im.crop((left, top, right, bottom))
        #     im.save('code.png')
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
        # driver.find_element_by_xpath('//*[@id="code"]').send_keys(getChar())  # 读取验证码并输入
        # time.sleep(8)
        # driver.find_element_by_xpath('//*[@onclick= "submitL();"]').click()  # 点提交登录
        # time.sleep(15)
        # a = driver.switch_to.alert
        #
        # def is_alert_on():  # 定义一个判断是否有弹框的方法。
        #     try:
        #         t = a.text
        #         return True
        #     except:
        #         return False
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
        #     driver.find_element_by_xpath('//*[@id="code"]').clear()
        #     time.sleep(1)
        #     driver.find_element_by_xpath('//*[@id="code"]').send_keys(getChar())
        #     time.sleep(3)
        #     driver.find_element_by_xpath('//*[@onclick= "submitL();"]').click()  # 点登录
        #     time.sleep(12)
        # if is_alert_on():  # 如果弹框出来了，就点确定
        #     a.accept()
        #     time.sleep(5)
        # else:  # 否则就通过了
        #     pass
        time.sleep(10)
        driver.find_element_by_xpath("//*[text()='预（销）售许可管理']").click()
        driver.find_element_by_id("c62a80f5-48b8-40be-8946-97fcc9d227be销控表").click()  # 点击销控表
        time.sleep(15)
        driver.switch_to.default_content()  # 回到默认顶层
        a = driver.find_elements_by_tag_name("iframe")[1]  # 切到第2个iframe
        driver.switch_to.frame(a)
        time.sleep(5)
        driver.find_element_by_xpath(
            "//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div").click()  # 点项目
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/div").click()  # 点自然幢
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='treeboxbox_tree']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[4]/span").click()  # 点逻辑幢
        time.sleep(2)
        # driver.find_element_by_xpath("//*[text()='A栋']").click()  #点逻辑幢
        time.sleep(5)
        driver.find_element_by_xpath("//*[text()='图形显示']").click()  # 点图形显示
        time.sleep(2)
        # driver.find_element_by_xpath("//*[@id='table_houseview']/tbody/tr[1]/td[3]/span[1]").click() #点201房屋
        driver.find_element_by_xpath("//*[@id='table_houseview']/tbody/tr[2]/td[3]/span[1]").click()  # 点103房屋
        time.sleep(5)
        # driver.switch_to_default_content()
        # ht = driver.find_elements_by_xpath("//*[@id='index']/div[4]/div[2]/div[2]/div/div/div/div[4]/div/iframe")
        # driver.switch_to_frame(ht)
        driver.switch_to.default_content()
        ht = driver.find_elements_by_tag_name("iframe")[2]  # 切换iframe  切换第3个iframe  有正式签订iframe
        driver.switch_to.frame(ht)
        driver.find_element_by_id("btn_zsht").click()  # 点正式签订
        time.sleep(60)
        driver.switch_to.default_content()
        ht1 = driver.find_elements_by_tag_name("iframe")[3]  # 切换iframe到第4个iframe  选合同模板的iframe
        driver.switch_to.frame(ht1)
        driver.find_element_by_xpath("//*[@name= 'mknameip']/option[1]").click()  # 选择合同模板
        time.sleep(5)
        driver.find_element_by_xpath("//*[@onclick = 'doChangeName()']").click()  # 点确定
        time.sleep(60)
        driver.switch_to.default_content()
        ht2 = driver.find_elements_by_tag_name("iframe")[3]  # 切换iframe 切换第4给iframe
        driver.switch_to.frame(ht2)
        driver.switch_to.frame("iframeshow")  # 切换到新增按钮的iframe
        # c= driver.find_elements_by_tag_name("iframe")[0] # 切换到新增按钮的iframe
        # driver.switch_to_frame(c)  # 切换到新增按钮的iframe
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id= 'gyfsSelect']/option[2]").click()  # 选择共有方式
        time.sleep(8)
        driver.find_element_by_id("btnAddMsr").click()  # 点新增买受人
        # f= driver.find_elements_by_tag_name("iframe")[1] # 切换到新增按钮的iframe
        # driver.switch_to_frame(f)  # 切换到新增按钮的iframe
        r = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/iframe")
        driver.switch_to.frame(r)  # 切换到输入买受人的iframe 是在上一个iframe里面的
        time.sleep(5)
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//*[@id='MSRMC']").send_keys("张会计")  # 输入买受人姓名
        driver.find_element_by_xpath("//*[@id= 'msrlx']/option[2]").click()  # 选择买受人类型
        driver.find_element_by_xpath("//*[@id = 'FDDBR']").send_keys("张丽")  # 输入法定代表
        # driver.find_element_by_xpath("//*[@id= 'hjszdlx']/option[3]").click()#选择国籍
        driver.find_element_by_xpath("//*[@id= 'ZJLXDM']/option[1]").click()  ##选择证件类型
        driver.find_element_by_id("zh").clear()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='zh']").send_keys("420804199005231122")  # 输入身份证
        driver.find_element_by_xpath("//*[@id= 'SFGSD']/option[2]").click()  # 选择户籍所在地
        # driver.find_element_by_id("zyfe").send_keys("56%") #输入共有份额
        driver.find_element_by_xpath("//*[@class='samllinput Wdate']").send_keys("2019-05-19")  # 输入出生日期
        driver.find_element_by_xpath("//*[@id= 'xb']/option[3]").click()  # 输入性别
        driver.find_element_by_id("msrdz").send_keys("江门市新会区101号")  # 输入地址
        driver.find_element_by_id("msryb").send_keys("456567")  # 输入邮编
        driver.find_element_by_xpath("//*[@class = 'samllinput']").send_keys("13454345678")  # 输入电话
        time.sleep(5)
        driver.find_element_by_id("btnConfirm").click()  # 新增买受人点确定
        time.sleep(60)
        driver.switch_to.default_content()
        ht2 = driver.find_elements_by_tag_name("iframe")[3]  # 切换iframe 切换第4给iframe
        driver.switch_to.frame(ht2)
        driver.switch_to.frame("iframeshow")  # 切换到新增按钮的iframe
        driver.find_element_by_id("nextpagebt").click()  # 点下一页
        time.sleep(5)
        # 第二章  商品房基本状况
        driver.implicitly_wait(3)
        # driver.find_element_by_xpath("//*[@id = 'JSGCGHXKZH']").send_keys("WYE666666") #输入建设工程规划许可证号为
        # driver.find_element_by_xpath("//*[@id = 'JZGCSGXKZH']").send_keys("WYE888888") #输入建筑工程施工许可证号
        # driver.find_element_by_xpath("//*[@id = 'jzztjg_s']").send_keys("钢和钢筋混凝土结构") #输入钢和钢筋混凝土结构
        # driver.find_element_by_xpath("//*[@id = 'jzzcs']").send_keys("8") #输入总层数
        # driver.find_element_by_xpath("//*[@id = 'dscs']").send_keys("7") #输入地上层
        # driver.find_element_by_xpath("//*[@id = 'dxcs']").send_keys("1") #输入地下层
        # driver.find_element_by_xpath("//*[@id = 'zlx']").send_keys("幢") #输入幢
        # driver.find_element_by_xpath("//*[@id = 'dy']").send_keys("1") #输入单元
        # driver.find_element_by_xpath("//*[@id= 'fhmc']/option[4]").click()#选择分户类型
        # driver.find_element_by_xpath("//*[@id = 'cg']").send_keys("24") #输入层高
        # driver.find_element_by_xpath("//*[@id = 'yt']").send_keys("2") #输入阳台
        # driver.find_element_by_xpath("//*[@id = 'fbsyt']").send_keys("1") #输入封闭式阳阳台
        # driver.find_element_by_xpath("//*[@id = 'ffbsyt']").send_keys("2") #输入非封闭式阳台
        # driver.find_element_by_xpath("//*[@id = 'qlzkcnlx']").send_keys("6") #输入同期贷款基准利率
        driver.find_element_by_id("nextpagebt").click()  # 点下一页
        # 第三章 商品房价款
        time.sleep(3)
        # driver.find_element_by_xpath("//*[@id = 'zjk1']").send_keys("300000") #输入总价格
        time.sleep(2)
        # driver.find_element_by_xpath("//*[@id = 'dj']").send_keys("10000") #输入定金
        # driver.find_element_by_xpath("//*[@id = 'djyy']").send_keys("抵作") #输入方式
        # driver.find_element_by_xpath("//*[@id = 'djzfsj']").send_keys("本合同签订") #输入方式
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id = 'qkzzzfrq1']").send_keys("2019-06-02")  # 输入一次付时间
        time.sleep(2)
        # driver.find_element_by_xpath("//*[@id = 'fkwyjbl1']").send_keys("8") #输入第九条  逾期付款责任
        # driver.find_element_by_xpath("//*[@id = 'yqfkts']").send_keys("5") #输入第九条  逾期付款责任
        driver.find_element_by_id("nextpagebt").click()  # 点下一页
        time.sleep(2)
        # 第四章  商品房交付条件与交付手续
        driver.find_element_by_xpath("//*[@id= 'jftj3']/option[2]").click()  # 选择第3条
        time.sleep(5)
        # driver.find_element_by_xpath("//*[@id = 'jftj3nr']").send_keys("健康的方式") #输入第九条  逾期付款责任
        # driver.find_element_by_xpath("//*[@id = 'jfrq']").send_keys("2019-06-02") #输入交付日期
        # driver.find_element_by_xpath("//*[@id = 'yqjfts']").send_keys("5") #输入第十二条  逾期交付责任
        # driver.find_element_by_xpath("//*[@id = 'jfwyjbl1']").send_keys("5") #输入第十二条  逾期交付责任
        # driver.find_element_by_xpath("//*[@id = 'yqjfts1']").send_keys("5") #输入第十二条  逾期交付责任
        # driver.find_element_by_xpath("//*[@id = 'jfwyjbl2']").send_keys("5") #输入第十二条  逾期交付责任
        driver.find_element_by_id("nextpagebt").click()  # 点下一页
        time.sleep(2)
        # 第五章  面积差异处理方式
        time.sleep(3)
        # driver.find_element_by_xpath("//*[@id = 'wcmjfklx1']").send_keys("5") #输入第十三条  面积差异处理
        # driver.find_element_by_xpath("//*[@id = 'wcmjfklx2']").send_keys("5") #输入第十三条  面积差异处理
        driver.find_element_by_id("nextpagebt").click()  # 点下一页
        time.sleep(2)
        # 第六章  规划设计变更
        time.sleep(3)
        # driver.find_element_by_xpath("//*[@id = 'ghbglx']").send_keys("5") #输入第十四条  规划变更
        # driver.find_element_by_xpath("//*[@id = 'ghbgwyjbl']").send_keys("5") #输入第十四条  规划变更
        # driver.find_element_by_xpath("//*[@id = 'ghbgyd']").send_keys("20190602化肥挥发") #输入第十四条  规划变更
        driver.find_element_by_id("nextpagebt").click()  # 点下一页
        time.sleep(2)
        # 第七章 商品房质量及保修责任
        time.sleep(5)
        # driver.find_element_by_xpath("//*[@id = 'kqgslx']").send_keys("2")
        driver.find_element_by_id("nextpagebt").click()  # 点下一页
        time.sleep(5)
        # 第八章  合同备案与房地产登记
        driver.find_element_by_xpath("//*[@id = 'syqzts']").send_keys("6")  # 输入第二十条  房地产登记
        driver.find_element_by_id("nextpagebt").click()  # 点下一页
        # 第九章  前期物业管理
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id = 'wyfwkssj']").send_keys("2019-06-02")
        driver.find_element_by_xpath("//*[@id = 'wyfwjssj']").send_keys("2022-06-02")
        driver.find_element_by_id("nextpagebt").click()  # 点下一页
        # 第十章  其他事项
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id = 'sfsx']").send_keys("国家")  # 输入第二十三条  税费
        driver.find_element_by_xpath("//*[@id = 'sdfs']").send_keys("邮寄挂号信")  # 输入第二十五条  送达
        driver.find_element_by_xpath("//*[@id = 'sdts']").send_keys("5")  # 输入第二十五条  送达

        driver.find_element_by_xpath("//*[@id = 'htys']").send_keys("56")  # 输入第二十九条  合同生效
        driver.find_element_by_xpath("//*[@id = 'htzfs']").send_keys("5")  # 输入第二十九条  合同生效
        driver.find_element_by_xpath("//*[@id = 'htcmrfs']").send_keys("3")  # 输入第二十九条  合同生效
        driver.find_element_by_xpath("//*[@id = 'htmsrfs']").send_keys("2")  # 输入第二十九条  合同生效
        driver.find_element_by_xpath("//*[@id = 'htzsr3']").send_keys("合作")  # 输入第二十九条  合同生效
        driver.find_element_by_xpath("//*[@id = 'htzs3fs']").send_keys("2")  # 输入第二十九条  合同生效
        driver.find_element_by_xpath("//*[@id = 'htzsr4']").send_keys("愉快")  # 输入第二十九条  合同生效
        driver.find_element_by_xpath("//*[@id = 'htzs4fs']").send_keys("2")  # 输入第二十九条  合同生效
        driver.find_element_by_xpath("//*[@id = 'btnSubmitZsHt']").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@class= 'dhtmlx_popup_button']").click()
        driver.switch_to.default_content()
        ht2 = driver.find_elements_by_tag_name("iframe")[3]  # 切换iframe 切换第4给iframe
        driver.switch_to.frame(ht2)
        driver.switch_to.frame("iframeshow")  # 切换到新增按钮的iframe
        r = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/iframe")
        driver.switch_to.frame(r)  # 切换到输入买受人的iframe 是在上一个iframe里面的
        time.sleep(5)
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//*[@id = 'MM']").send_keys("123123")  # 输入
        driver.find_element_by_xpath("//*[@id = 'RMM']").send_keys("123123")  # 输入
        driver.find_element_by_xpath("//*[@id = 'btnConfirm']").click()

