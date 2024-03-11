#-- coding: utf-8 --

#@Time : 2022/9/16 16:27

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : 查询数据库数据导出到excel.py

#@Software: PyCharm

import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd
from sqlalchemy import create_engine
"""
pip3 install sqlalchemy psycopg2 pandas openpyxl
"""
# engine = create_engine('dialect+driver://username:password@host:port/database')
engine = create_engine('mysql://luf99:9900@192.168.13.53:3306/zentao')

sql = "select * from zt_project"

df = pd.read_sql(sql, engine)
print(df.head())

df.to_excel('禅道项目表(zt_project).xlsx', index=None)