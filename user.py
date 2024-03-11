#-- coding: utf-8 --

#@Time : 2022/12/14 13:20

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : user.py

#@Software: PyCharm
from flask import Blueprint, render_template, session, url_for,request,redirect
# from werkzeug.utils import redirect

user=Blueprint('user',__name__)    #蓝图使用方法，参数里给定文件名，还可以给定url前缀

@user.route('/login')   #使用user的路由配置
def loginpage():
    return render_template("login.html")

@user.route('/loginProcess',methods=['POST','GET'])   #使用user 的路由配置
def loginProcesspage():
    if request.method=='POST':
        nm=request.form['nm']
        pwd=request.form['pwd']
        if nm=='cao' and pwd=='123':
            session['username']=nm
            print(session['username'])
            return redirect(url_for('selectpropage'))
        else:
            return 'the username or userpwd does not match!'
