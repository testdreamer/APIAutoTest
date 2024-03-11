#-- coding: utf-8 --

#@Time : 2022/7/15 13:33

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : cennect_mysql_zentao.py

#@Software: PyCharm
import pymysql


class ConnectMysqlZentao:

    """数据库连接配置"""
    # def __init__(self):
    #     self.host = '192.168.13.53'
    #     self.port = 3306
    #     self.user = 'luf99'
    #     self.passwd = '9900'
    #     self.db = 'zentao'
    #     self.charset = 'utf8'

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.passwd = '123456'
        self.db = 'zentao'
        self.charset = 'utf8'

    # def __init__(self):
    #     self.host = '192.168.13.188'
    #     self.port = 3306
    #     self.user = 'root'
    #     self.passwd = 'Lyyl@2020'
    #     self.db = 'zentao'
    #     self.charset = 'utf8'

    '''打开数据库连接'''
    def connect_zentao(self):
        try:
            db = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                charset=self.charset)
            # 获取游标
            cursor = db.cursor()
        except ConnectionError:
            print("===Mysql连接失败，检查连接信息===")
        return db, cursor

    '''关闭数据库连接'''
    def close_mysql_zentao(self, db):
        try:
            db.close()
        except IOError:
            print("===关闭数据库连接异常===")
    '''查询数据库数据'''
    def get_select_data_zentao(self, sql):
        db, cursor = self.connect_zentao()
        # try:
            # 执行SQL语句
        cursor.execute(sql)
        # 获取所有查询结果
        try:
            results = cursor.fetchall()
        except Exception:
            print("===执行sql报错===")
        finally:
            self.close_mysql_zentao(db)
        return results

    '''更改（增、删、改）数据库数据'''

    def change_data_zentao(self, sql):
        db, cursor = self.connect_zentao()
        # try:
            # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        try:
            db.commit()
        except Exception:
            # 发生错误时回滚
            db.rollback()
            print("删除错误，删除已回滚")
        finally:
            self.close_mysql_zentao(db)