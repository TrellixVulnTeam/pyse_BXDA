# encoding: utf-8
"""
@author: suchao
@file: run.py
@time: 2018/11/5 14:21
@desc:调用cmd，执行用例，并且生成Allure测试报告
"""
import pytest
import os
from utils.shell import Shell
from utils.utils import cleanfolder

if __name__ == '__main__':
    # 获取Report\xml和Report\html的路径
    xml_report_path = os.path.join(os.getcwd(), "report\\json")
    html_report_path = os.path.join(os.getcwd(), "report\\html")
    set_browser = "--browser=chrome"

    cleanfolder(xml_report_path)
    # 开始测试
    args = ['-s', '-q', '--alluredir', xml_report_path, set_browser]
    pytest.main(args)

    # 生成html测试报告
    cmd = 'allure generate --clean %s -o %s' % (xml_report_path, html_report_path)

    try:
        Shell.invoke(cmd)
    except:
        print ("Test Failed")
    finally:
        print ("Test Completed")