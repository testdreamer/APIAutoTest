#-- coding: utf-8 --

#@Time : 2022/9/14 10:01

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : runMain_all.py

#@Software: PyCharm
import runMain_udaam_a
import os,sys
from Utils.operationyaml import *
import pytest
if __name__ == '__main__':
    # os.chdir(sys.path[0])
    # pro_select_file = 'http://192.168.13.148:63805/udaam/project_name.txt'
    # original_file = sys.path[-1] + '/project_name.txt'
    # from_wget_download_file(pro_select_file, original_file)
    # pro_select_value = read_yaml_no_key(original_file)

    # if pro_select_value == 'udaam':
    #     os.system('python runMain_udaam_a.py')
    #     # os.system('python runMain_remote_udaam_a.py')
    #
    # elif pro_select_value == 'udemr':
    #     os.system('python runMain_udemr_p.py')
    # else:
    #     print('选择项目名称错误!')


    os.system('python runMain_udemr_s.py udaam')



if __name__ == '__main__':
    pytest.main()