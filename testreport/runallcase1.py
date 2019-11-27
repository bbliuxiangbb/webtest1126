#@Author: LIUXIANG
#@Time  :  2019/9/29 18:03


import unittest
import  time
from BeautifulReport import  BeautifulReport
from common import BeautifulReport_cn
#用例路径
suite_tests = unittest.defaultTestLoader.discover( r"C:\Users\Administrator\PycharmProjects\web_test\\testcase", pattern="test*.py",top_level_dir=None)
# 取前面时间
print(suite_tests)
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
filename = now + '.html'
result = BeautifulReport(suite_tests)
result.report(filename='测试报告20191021', description='各子系统查询、引用、调档正常业务功能测试', log_path='.')



