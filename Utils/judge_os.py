#-- coding: utf-8 --

#@Time : 2022/9/28 10:18

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : judge_os.py

#@Software: PyCharm
from sys import platform

if ("linux" == platform) or ("linux2" == platform):
    print("Linux")
elif ("win32" == platform):
    print("win32")
else:
	print("Others")