#-- coding: utf-8 --

#@Time : 2023/1/4 10:17

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : performanceauto.py

#@Software: PyCharm
from flask import Blueprint, render_template,request,flash
from werkzeug.utils import secure_filename
import os,sys
from Utils.log import *
from sys import platform
performanceauto=Blueprint('performanceauto',__name__)

@performanceauto.route('/performanceauto')
def apiautopage():
    return render_template("performanceauto.html")

@performanceauto.route('/performanceautouploader',methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        f = request.files.getlist('file')
        print(request.files)
        dd = []
        for fi in f:
            suffix = fi.filename.split('.')[-1]
            system_id = fi.filename.split('_')[0]
            # 根据当前操作系统,按被测项目名创建配置文件文件夹
            data_path = sys.path[0] + '\p_udemr\\data\\' + system_id
            if ("linux" == platform) or ("linux2" == platform):
                os.system('mkdir ' + data_path.replace('\\', '/'))
            elif ("win32" == platform):
                os.system('md ' + data_path)
            else:
                log.info("----------Others-----------")

            # 根据当前操作系统,按被测项目名创建测试用例文件夹
            testcase_path = sys.path[0] + '\p_udemr\\test_cases\\' + system_id
            if ("linux" == platform) or ("linux2" == platform):
                os.system('mkdir ' + testcase_path.replace('\\', '/'))
            elif ("win32" == platform):
                os.system('md ' + testcase_path)
            else:
                log.info("----------Others-----------")


            if suffix == 'jmx':
                fi.save(os.path.join(testcase_path, fi.filename))
            else:
                fi.save(os.path.join(data_path, fi.filename))
        pro = request.form['pro'].replace('电子病历','udemr')
        flash('Please enter all the fields', 'error')
        # os.system('python runMain_apiauto_flask.py ' + pro)
        # get_console_output = os.popen('runMain_performanceauto_flask.py ' + pro)
        # for line in get_console_output.readlines():
        return render_template('performanceauto.html',data=dd)
    else:
        return render_template('upload.html')
