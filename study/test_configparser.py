# _*_ coding : utf_8 _*_
# @Time : 17:49 
# @Author : 田霄汉
# @File : test_configparser
# @Project : APIAutoTest
# @User : Administrator
import os.path

from Utils.conf import *

cf = Conf()
iniPath = os.path.dirname(__file__)+'/data/appscan_config.ini'


# # 读取ini文件，后面get()依赖于read()方法
# cf.read(iniPath, encoding='utf-8')
# res = cf.get('section06', 'option06')
# print(res)


# 对ini文件进行新增section
cf.add_section('section06')
cf.set('section06', 'option06', 'value')

cf.items()
# 对ini文件增删该查则需要最后把内容写入到文件里面
with open(iniPath, 'a', encoding='utf-8') as f:
    cf.write(f)