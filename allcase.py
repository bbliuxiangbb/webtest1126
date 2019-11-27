
import unittest
from common import HTMLTestRunner_cn
#用例路径
casePath = r"C:\Users\Administrator\PycharmProjects\web_test\\testcase"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover( start_dir=casePath,pattern= rule)
print(discover)
reportPath =r"C:\Users\Administrator\PycharmProjects\web_test\testreport\\" +"report1127.html"
fp = open(reportPath,"wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream= fp ,
                                          title = "从业主体系统，诚信管理系统，存量房管理系统，预售资金系统，商品房合同管理系统，统计分析系统各菜单调查询，引用，调档，保存，提交测试",
                                          description = "由于开发改了很多业务的问题，或者是公共的方法，对于禅道没有涉及的业务，也没测试到，那么查询，调档，引用测试就可以帮助发现一些问题存在"

                                           )
runner.run(discover)

fp.close()
