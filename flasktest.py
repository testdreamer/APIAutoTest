#-- coding: utf-8 --

#@Time : 2022/12/13 11:25

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : flasktest.py

#@Software: PyCharm
from flask import Flask, render_template,request,redirect,url_for,session,g
from news import news         #导入news蓝图
from user import user        #导入user蓝图
from product import product   #导入product蓝图
from safe import safe
from apiauto import apiauto
from performanceauto import performanceauto
import dbutil  # 导入dbutil模块，就是上面这个文件
app = Flask(__name__)
app.secret_key='any random string'    #这里我们直接给定一个密钥
app.config['UPLOAD_FOLDER'] = 'upload/'
urls=[news,user,product,safe,apiauto,performanceauto]      #将三个路由构建数组
for url in urls:
    app.register_blueprint(url)   #将三个路由均实现蓝图注册到主app应用上

@app.route('/')
def index():
    userinfo='fffffffffffffff'
    return render_template("index.html", data=userinfo)

@app.route('/selectpro')
def selectpropage():
    return render_template("selectpro.html")
# @app.route('/')
# def index():
#
#     db = dbutil.dbUtils('web2020.db')  # 链接web2020数据库
#     sql = 'select * from news'  # 组装查询sql语句
#     newslist = db.db_action(sql, 1)  # 查询处理并返回列表
#     db.close()
#     return render_template("index.html", data=newslist)
#
#
# @app.route('/news')  # 增加一个news页面
# def newspage():
#     newsContent = "全国上下一心支持武汉，武汉加油！"
#     return render_template("news.html", data=newsContent)
#
#
# # @app.route('/product')  # 增加一个product页面
#
#
# @app.route('/product/<a>',methods=['GET'])
# def productpage(a):
#     return render_template("product.html",data=a)
#
# @app.route('/login')
# def loginpage():
#     return render_template("login.html")
#
# @app.route('/loginProcess',methods=['POST','GET'])
# def loginProcesspage():
#     if request.method=='POST':
#         nm=request.form['nm']     #获取姓名文本框的输入值
#         pwd=request.form['pwd']   #获取密码框的输入值
#         if nm=='cao' and pwd=='123':
#             session['username'] = nm   #定义session
#             g.name = 'cao'   #定义全局变量
#             return redirect(url_for('index'))   #使用跳转html页面路由
#         else:
#             return 'the username or userpwd does not match!'

# context上下文处理可以在局部也可以在全局。例如想定义一下全局公用变量，可以采用如下方式：
# @app.context_processor
# def common():
#     isLogin=False
#     return isLogin
if __name__ == "__main__":
    print(app.url_map)  # 打印url结构图
    app.run(port=2020, host="0.0.0.0", debug=True)
