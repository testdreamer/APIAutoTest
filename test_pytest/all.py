# _*_ coding : utf_8 _*_
# @Time : 18:23 
# @Author : 田霄汉
# @File : all
# @Project : APIAutoTest
# @User : Administrator
import os

import pytest

if __name__ == '__main__':
    pytest.main(["./testcases/test_lbs_amap.py"])
    # pytest.main(["./testcases/test_juhe.py"])
    # pytest.main()
    # 生成allure报告的命令
    # os.system("allure generate temp -o reports --clean")
