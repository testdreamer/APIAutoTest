# -*- coding:utf-8 -*-
'''
@Author: tianxh
@Email : tianxh@casking.com.cn
@Time: 2022/12/4 18:05
@File: connectOracle.py
@Software: PyCharm
'''
import cx_Oracle as oracle

class ConnectOracle():
    '''测试环境'''
    def __init__(self):
        self.host = '192.168.13.83'
        self.port = 1521
        self.sid = 'ORCLCDB'
        self.user = 'udemr'
        self.password = 'Test1234'


    """连接Oracle数据库"""
    def connect_oracle(self):
        try:
            # 使用tns串连接
            dsn_tns = oracle.makedsn(self.host, self.port, self.sid)
            # 连接Oracle数据库
            conn = oracle.connect(user=self.user, password=self.password, dsn=dsn_tns)
            # 获取游标
            cursor = conn.cursor()
        except ConnectionError:
            print("===Oracle连接失败，检查连接信息===")
        return conn, cursor


    """关闭Oracle数据库"""
    def close_oracle(self):
        """
        :return: 无返回值
        """
        cursor, conn = self.connect_oracle()
        try:
            cursor.close()
        except IOError:
            print("===关闭数据库连接失败===")


    """查询数据库数据"""
    def excult_query_sql(self,sql):
        """
        :param sql: 查询sql语句，不要加分号';'
        :return: qryset
        """
        # sql中如果包含"；"或者";"，将其清除
        if ";" in sql:
            new_sql = sql.replace(";","")
        elif "；" in sql:
            new_sql = sql.replace("；","")
        else:
            new_sql =sql

        # 开始执行查询sql
        conn, cursor = self.connect_oracle()
        try:
            result = cursor.execute(new_sql)
            qryset = result.fetchall()
        except Exception:
            print("===执行sql语句报错===")
        finally:
            self.close_oracle()
        return qryset


    """执行sql语句并提交"""
    def excult_commit_sql(self, sql):
        """
        :param sql: 需要执行的sql语句
        :return: 无返回值
        """
        # sql中如果包含"；"或者";"，将其清除
        if ";" in sql:
            new_sql = sql.replace(";", "")
        elif "；" in sql:
            new_sql = sql.replace("；", "")
        else:
            new_sql = sql

        # 开始执行语句sql
        conn, cursor = self.connect_oracle()
        try:
            # 执行sql语句
            result = cursor.execute(new_sql)
            # 提交
            conn.commit()
        except Exception:
            # 提交报错，数据回滚
            conn.rollback()
            print("===sql语句报错，完成数据回滚===")
        finally:
            self.close_oracle()

    """直接执行Oracle查询sql"""
    def dirct_excult_query_sql(self, sql):
        '''
        执行Oracle SQL查询语句
        :param sql: sql语句，变量使用：var或者：1，：2表示
        :return: queryset
        '''
        # sql中如果包含"；"或者";"，将其清除
        if ";" in sql:
            new_sql = sql.replace(";", "")
        elif "；" in sql:
            new_sql = sql.replace("；", "")
        else:
            new_sql = sql

        # 开始连接Oracle数据并执行查询sql
        dsn_tns = oracle.makedsn(self.host, self.port, self.sid)
        print(dsn_tns)
        connection = oracle.connect(user=self.user, password=self.password, dsn=dsn_tns)
        cursor = connection.cursor()
        result = cursor.execute(new_sql)
        qryset = result.fetchall()
        cursor.close()
        connection.close()
        return qryset

    """直接执行Oracle变更sql"""
    def dirct_excult_commit_sql(self, sql):
        '''
        执行Oracle SQL执行语句
        :return: 无返回值
        '''
        # sql中如果包含"；"或者";"，将其清除
        if ";" in sql:
            new_sql = sql.replace(";", "")
        elif "；" in sql:
            new_sql = sql.replace("；", "")
        else:
            new_sql = sql

        # 开始连接Oracle数据并执行语句sql
        dsn_tns = oracle.makedsn(self.host, self.port, self.sid)
        connection = oracle.connect(user=self.user, password=self.password, dsn=dsn_tns)
        cursor = connection.cursor()
        cursor.execute(new_sql)
        connection.commit()
        cursor.close()
        connection.close()
