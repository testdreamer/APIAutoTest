import os.path
import random

from jsonpath import jsonpath
from contextlib import ExitStack
from Utils.operationyaml import *
import csv

def EnvReplaceYaml(yamlfile, new_yamlfile):

    """
    yamlfile：带有$csv{name}的yaml文件路径
    new_yamlfile：解析后的新yaml文件路径
    """
    # 获取根目录
    root_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    # 读取yaml文件里面的csv文件目录
    csv_file = os.path.abspath(os.path.join(root_file, jsonpath(read_yaml_no_key(yamlfile), '$..name-appid-secret-grant_type-assert_str')[0]))
    # 读取csv中的数据
    profileList = []
    with open(csv_file, 'r', encoding='utf') as csv_path:
        # csv.DictReader()
        reader = csv.DictReader(csv_path)
        for row in reader:
            profileList.append(dict(row))

    try:
        with ExitStack() as stack:
            yml_file = stack.enter_context(open(yamlfile, '+r'))
            yml_output = stack.enter_context(open(new_yamlfile, 'w'))
            # 按照lines读取yamlfile文件，返回值为字符串列表
            yml_file_lines = yml_file.readlines()
            # 循环遍历profileList的长度（即循环csv每行的数据）
            for i in range(0, len(profileList)):
                # 循环遍历yml_file生成的readlines()
                for line in yml_file_lines:
                    # new_line = line
                    # 判断如果找到以"$csv{"开头的line
                    if line.find('$csv{') > 0:
                        # # 对字符串以“$csv{”切割
                        # env_list = line.split('$csv{')
                        # 用"$csv{"切割取后半部分，再清除掉空格和字符，再以"}"切割取前半部分，这样可以取到key了
                        env_name = line.split('$csv{')[1].strip().split('}')[0]
                        replacement = ''
                        # 判断如果取到的name在cvs的解析的key值当中
                        if env_name in profileList[i].keys():
                            # 使用replacement接收csv文件中key的value值
                            replacement = profileList[i][env_name]
                            # for j in range(0, len(profileList)):
                            #     line = line.replace("$csv{"+env_name+"}", replacement)
                            # 将取到的csv文件中的key的value值对yaml文件中的line中的$csv{key}进行替换
                            line = line.replace("$csv{" + env_name + "}", replacement)
                    # 将line写入到yml_output文件
                    yml_output.write(line)
                # 完成每行csv文件的数据后面加两个换行符
                yml_output.write('\n\n')

    except IOError as e:
        print("Error: "+format(str(e)))
        raise