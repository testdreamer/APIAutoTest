#-- coding: utf-8 --#@Time : 2022/5/20 13:24#@Author : tianxh#@Email : 729560832@qq.com#@File : test_appscan.py#@Software: PyCharm# import unittest# import os# from Utils.page import *# import pywinauto# import time# import lackey# import sys,os# from Utils.log import *# from Utils.operationini import Conf# from pywinauto.keyboard import *# from pywinauto.mouse import *# import time# # from pywinauto.keyboard import mouse# sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))# # class Totasks(unittest.TestCase,Helper):## def test_bd(path):#     appscan_config_ini = sys.path[1] + '\\a_safety\data\\appscan_config.ini'#     Photo_url = sys.path[1]+'\Safety\Photo\\'#     cf = Conf#     # 启动exe#     # path = "C:\Program Files (x86)\HCL\AppScan Standard\AppScan.exe"#     app = pywinauto.Application().start(path)#     time.sleep(10)#     lackey.click(Photo_url+'chuangjianweb.png')#     time.sleep(2)#     lackey.click(Photo_url + 'shuruurl.png')#     time.sleep(2)#     lackey.type(cf.getini_by_section(appscan_config_ini,'起始url').get('url'))#     time.sleep(15)#     lackey.click(Photo_url+ 'xiugaiurl.png')#     lackey.type('s')#     time.sleep(2)#     lackey.click(Photo_url+'xiayibu.png')#     time.sleep(2)#     lackey.click(Photo_url+'Record.png')#     time.sleep(2)#     lackey.click(Photo_url+ 'appscanChromium.png')#     time.sleep(12)#     lackey.click(Photo_url+ 'fangdachuangkou.png')#     time.sleep(2)#     lackey.click(Photo_url+ 'shuruzhanghao.png')#     lackey.type(cf.getini_by_section(appscan_config_ini,'被测网站').get('username'))#     time.sleep(5)#     lackey.click(Photo_url+ 'shurumima.png')#     lackey.type(cf.getini_by_section(appscan_config_ini,'被测网站').get('password'))#     time.sleep(5)#     lackey.click(Photo_url + 'shuruyanzhengma.png')#     lackey.type(cf.getini_by_section(appscan_config_ini,'被测网站').get('code'))#     log.info('输入code')#     time.sleep(5)#     lackey.click(Photo_url + 'denglu.png')#     log.info('登录')#     time.sleep(2)#     lackey.click(Photo_url + 'iamloginintothesite.png')#     log.info('iamloginintothesite')#     time.sleep(35)#     lackey.click(Photo_url+ 'guanbi.png')#     log.info('关闭')#     time.sleep(2)#     lackey.click(Photo_url + 'jixu.png')#     time.sleep(30)#     lackey.click(Photo_url + 'xiayibu2.png')#     time.sleep(2)#     lackey.click(Photo_url+ 'xiayibu2.png')#     time.sleep(2)#     lackey.click(Photo_url+ 'xiayibu2.png')#     # time.sleep(2)#     # lackey.click(sys.path[1] + '\Photo\\' + 'next.png')#     time.sleep(2)#     lackey.click(Photo_url + 'wancheng.png')#     time.sleep(2)#     lackey.click(Photo_url + 'shi.png')#     time.sleep(2)#     lackey.click(Photo_url + 'baocun.png')#     lackey.type(time.strftime("%Y_%m_%d_%H_%M_%S"))#     time.sleep(2)#     lackey.click(Photo_url + 'jiaobenbaocun.png')#     time.sleep(2)#     # 调用exe程序#     # os.startfile("C:\Program Files (x86)\HCL\AppScan Standard\AppScan.exe")