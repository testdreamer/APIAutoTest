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
from test_pytest.Utils.envreplaceyaml import *



@pytest.fixture(scope="function")
def connectDB():
    print("连接数据库成功")
    yield
    print("关闭连接数据库")

# @pytest.fixture(scope="session", autouse=True)
# def birth_replaceyaml():
#     """
#     对yaml文件进行解析$csv{name}
#     yamlfile: 需要解析的yaml文件
#     new_yamlfile: 解析成功后的yaml文件
#     return:
#     """
#     new_yamlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '../birthToLuck.yml'))
#     yamlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '../old_birthToLuck.yml'))
#     EnvReplaceYaml(yamlfile, new_yamlfile)
#     yield
#     clear_yaml(new_yamlfile)
#
# @pytest.fixture(scope="session", autouse=True)
# def QQ_replaceyaml():
#     """
#     对yaml文件进行解析$csv{name}
#     yamlfile: 需要解析的yaml文件
#     new_yamlfile: 解析成功后的yaml文件
#     return:
#     """
#     new_yamlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '../QQToLuck.yml'))
#     yamlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '../old_QQToLuck.yml'))
#     EnvReplaceYaml(yamlfile, new_yamlfile)
#     yield
#     clear_yaml(new_yamlfile)
#
# @pytest.fixture(scope="session", autouse=True)
# def IP_replaceyaml():
#     """
#     对yaml文件进行解析$csv{name}
#     yamlfile: 需要解析的yaml文件
#     new_yamlfile: 解析成功后的yaml文件
#     return:
#     """
#     new_yamlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_IP_location.yml'))
#     yamlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '../old_test_IP_location.yml'))
#     EnvReplaceYaml(yamlfile, new_yamlfile)
#     yield
#     clear_yaml(new_yamlfile)
#
# @pytest.fixture(scope="session", autouse=True)
# def weather_replaceyaml():
#     """
#     对yaml文件进行解析$csv{name}
#     yamlfile: 需要解析的yaml文件
#     new_yamlfile: 解析成功后的yaml文件
#     return:
#     """
#     new_yamlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_weather_forecast.yml'))
#     yamlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '../old_test_weather_forecast.yml'))
#     EnvReplaceYaml(yamlfile, new_yamlfile)
#     yield
#     clear_yaml(new_yamlfile)

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