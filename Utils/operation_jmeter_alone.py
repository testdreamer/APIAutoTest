#-- coding: utf-8 --

#@Time : 2022/9/30 16:20

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : operation_jmeter_alone.py

#@Software: PyCharm
from Utils.operation_remote_server import *
from Utils.operationini import *
cf = Conf
def read_config_file_download_linux():
    jmeter_script_config = sys.path[-1] + '/p_udemr/data/jmeter_script_config.ini'
    jmeter_script_name = cf.getini_by_option(jmeter_script_config,'jmeter脚本名称','jmeter_script_name')
    local_jmx = sys.path[-1] + '/' + 'p_udemr' + '/' + 'test_cases' + '/' + jmeter_script_name+'.jmx'
    remote_jmx = '/usr/local/jmeter/apache-jmeter-5.1.1/scripts/'+jmeter_script_name+'.jmx'
    file_download_linux('192.168.13.69', 'root', 'UT@123', remote_jmx,local_jmx)