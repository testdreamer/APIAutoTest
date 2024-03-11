#-- coding: utf-8 --

#@Time : 2022/12/30 17:43

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : apiauto.py

#@Software: PyCharm
from flask import Blueprint, render_template,request
from werkzeug.utils import secure_filename
import os
apiauto=Blueprint('apiauto',__name__)

@apiauto.route('/apiauto')
def apiautopage():
    return render_template("apiauto.html")

@apiauto.route('/uploader',methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        f.save(os.path.join('./api_auto_excel/test_cases', f.filename))
        # f.save(secure_filename(f.filename))
        pro = request.form['pro']
        # os.system('python runMain_apiauto_flask.py ' + pro)
        get_console_output = os.popen('python runMain_apiauto_flask.py ' + pro)
        for line in get_console_output.readlines():
            return render_template('apiauto.html',data=line)
    else:
        return render_template('upload.html')
