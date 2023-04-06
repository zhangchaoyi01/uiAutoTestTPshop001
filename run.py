import os
import time
import unittest
from config import BASE_PATH
from scripts.test_login import TestLogin
from tools.HTMLTestReportCN import HTMLTestRunner


if __name__ == '__main__':
    # 1.初始化suite对象
    suite = unittest.TestSuite()
    # 2.组装测试案例  注意：用测试套件运行不起来，有可能跟组装测试案例的方法有关系，换个方法，我也不知道什么原因
    # suite.addTest(TestLogin("test_login"))
    suite.addTest(unittest.makeSuite(TestLogin))
    # 3.报告存放路径
    file_path = BASE_PATH + os.sep + "report" + os.sep
    # 4.获取当前时间
    new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    # 5.准备测试报告名称
    report_name = file_path + new_time + "_report.html"
    # 6.开启报告写入文件流  b代表二进制
    with open(report_name, "wb") as f:
        # 初始化报告执行对象
        runner = HTMLTestRunner(stream=f,
                                verbosity=2,
                                title="TPshop登录模块自动化测试报告",
                                description="测试平台：windows 版本：v1.2",
                                tester="QA")
        # 7.执行suite
        runner.run(suite)
