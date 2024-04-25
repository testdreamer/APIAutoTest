# _*_ coding : utf_8 _*_
# @Time : 1:16 
# @Author : 田霄汉
# @File : study
# @Project : APIAutoTest
# @User : Administrator
import os

# from jsonpath import jsonpath
#
# from Utils.operationyaml import read_yaml_no_key
# from test_pytest.Utils.operationyaml import YamlUtils

# from test_pytest.Utils.operationyaml import *
# YamlUtils().clear_yaml(filename=os.path.abspath(os.path.join(os.getcwd(), "../extract.yml")))
# # result = read_yaml_no_key(filename=os.path.abspath(os.path.join(os.getcwd(), "../extract.yml")))
# # print(result['yangli'])
# # print(result['wuxing'])
# # print(result['conclusion'])
# result = {'status': '1', 'count': '1', 'info': 'OK', 'infocode': '10000', 'lives': [{'province': '北京', 'city': '东城区', 'adcode': '110101', 'weather': '晴', 'temperature': '17', 'winddirection': '东', 'windpower': '≤3', 'humidity': '61', 'reporttime': '2024-04-21 23:03:04', 'temperature_float': '17.0', 'humidity_float': '61.0'}]}
# if "province" in result:
#     print("[]为真")
# extract_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../extract.yml'))
# verify_data = YamlUtils().read_yaml_no_key(filename=extract_file)
# print(verify_data)
# if verify_data is None:
#     print("niubi")
# import csv
# root_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
# yamlfile = os.path.abspath(os.path.join(root_file, "study/data/test.yaml"))
# csv_file = os.path.abspath(os.path.join(root_file, jsonpath(read_yaml_no_key(yamlfile), '$..name-appid-secret-grant_type-assert_str')[0]))
# profileList = []
# with open(csv_file, 'r', encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         profileList.append(dict(row))

# testDict = {'reason': 'æ\x8e¥å\x8f£å\x9c°å\x9d\x80ä¸\x8då\xad\x98å\x9c¨', 'result': None, 'error_code': 10022}
# testStr = "conclusion1"
# # if testStr not in testDict:
# #     print("这是真的")
# print(type(testDict["result"]))

# extract_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../extract.yml'))
# result = YamlUtils().read_yaml_no_key(filename=extract_file)
# # if YamlUtils().read_yaml_no_key(filename=extract_file) == None:
# #     YamlUtils().write_yaml_add(dataurl=extract_file, content={"content":"test"})
# if "abc" not in str(result):
#     YamlUtils().write_yaml_add(dataurl=extract_file, content={"content":"test"})

# from test_pytest.Utils.envreplaceyaml import *
# yamlfile01 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../old_birthToLuck.yml"))
# new_yamlfile01 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../birthToLuck.yml"))
# yamlfile02 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../old_QQToluck.yml"))
# new_yamlfile02 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../QQToluck.yml"))
# yamlfile03 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../old_test_IP_location.yml"))
# new_yamlfile03 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../test_IP_location.yml"))
# yamlfile04 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../old_test_weather_forecast.yml"))
# new_yamlfile04 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../test_weather_forecast.yml"))
# EnvReplaceYaml(yamlfile=yamlfile01, new_yamlfile=new_yamlfile01)
# EnvReplaceYaml(yamlfile=yamlfile02, new_yamlfile=new_yamlfile02)
# EnvReplaceYaml(yamlfile=yamlfile03, new_yamlfile=new_yamlfile03)
# EnvReplaceYaml(yamlfile=yamlfile04, new_yamlfile=new_yamlfile04)


# import os.path
# from jsonpath import jsonpath
# from contextlib import ExitStack
# from Utils.operationyaml import *
# import csv
#
#
# yamlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), "../old_birthToLuck.yml"))
# new_yamlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), "../birthToLuck01.yml"))
#
# # 读取yaml文件里面的csv文件目录
# csv_file = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), "../"), jsonpath(read_yaml_no_key(yamlfile), '$..name-appid-secret-grant_type-assert_str')[0]))
#
# # print(csv_file)
#
#
#
# # 读取csv中的数据
# profileList = []
# with open(csv_file, 'r', encoding='UTF-8-sig') as csv_path:
#     # csv.DictReader()
#     reader = csv.DictReader(csv_path)
#     for row in reader:
#         profileList.append(dict(row))
#     print(profileList)

# try:
#     with ExitStack() as stack:
#         yml_file = stack.enter_context(open(yamlfile, '+r'))
#         yml_output = stack.enter_context(open(new_yamlfile, 'w'))
#         # 按照lines读取yamlfile文件，返回值为字符串列表
#         yml_file_lines = yml_file.readlines()
#         # 循环遍历profileList的长度（即循环csv每行的数据）
#         for i in range(0, len(profileList)):
#             # 循环遍历yml_file生成的readlines()
#             for line in yml_file_lines:
#                 # new_line = line
#                 # 判断如果找到以"$csv{"开头的line
#                 # print(line)
#                 if line.find('$csv{') > 0:
#                     # # 对字符串以“$csv{”切割
#                     # env_list = line.split('$csv{')
#                     # 用"$csv{"切割取后半部分，再清除掉空格和字符，再以"}"切割取前半部分，这样可以取到key了
#                     env_name = line.split('$csv{')[1].strip().split('}')[0]
#                     # print(env_name)
#                     replacement = ''
#                     # 判断如果取到的name在cvs的解析的key值当中
#                     if env_name in profileList[i].keys():
#                         # 使用replacement接收csv文件中key的value值
#                         replacement = profileList[i][env_name]
#                         print(replacement)
# #                         # for j in range(0, len(profileList)):
# #                         #     line = line.replace("$csv{"+env_name+"}", replacement)
# #                         # 将取到的csv文件中的key的value值对yaml文件中的line中的$csv{key}进行替换
# #                         line = line.replace("$csv{" + env_name + "}", replacement)
# #                 # 将line写入到yml_output文件
# #                 yml_output.write(line)
# #             # 完成每行csv文件的数据后面加两个换行符
# #             yml_output.write('\n\n')
# #
# except IOError as e:
#     print("Error: "+format(str(e)))
#     raise

# new_yamlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), "../back/birthToLuck.yml"))
#
# from test_pytest.Utils.operationyaml import *
#
# result = YamlUtils().read_yaml_no_key(new_yamlfile)
# print(result)


import pytest


# 定义一个fixture
@pytest.fixture
def setup_data():
    print("Fixture is running")
    return "fixture_data"


# 使用parametrize参数化测试
@pytest.mark.parametrize("data", ["param1", "param2"])
def test_example(setup_data, data):
    print(f"Testing with data: {data}")
    assert setup_data == "fixture_data"

if __name__ == '__main__':
    test_example()