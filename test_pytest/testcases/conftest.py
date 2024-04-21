# _*_ coding : utf_8 _*_
# @Time : 19:47 
# @Author : 田霄汉
# @File : conftest
# @Project : APIAutoTest
# @User : Administrator
import os

import pytest
from test_pytest.Utils.operationyaml import *
import os



@pytest.fixture(scope="function")
def connectDB():
    print("连接数据库成功")
    yield
    print("关闭连接数据库")

@pytest.fixture(scope='session', autouse=True)
def clear_extracyaml():
    """
    清除extrac.yaml文件内容
    :return:
    """
    YamlUtils().clear_yaml(filename=os.path.abspath(os.path.join(os.path.dirname(__file__), "../extract.yml")))
    # with open(filename, mode='w', encoding='utf-8') as f:
    #     f.truncate()
    #     f.close()
    print("清除yaml文件成功")