#-- coding: utf-8 --

#@Time : 2022/12/30 17:17

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : safe.py

#@Software: PyCharm
from flask import Blueprint, render_template
safe=Blueprint('safe',__name__)

@safe.route('/safe')
def safepage():
    return render_template("safe.html")
