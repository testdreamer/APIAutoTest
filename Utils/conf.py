#-- coding: utf-8 --

#@Time : 2022/5/16 11:11

#@Author : tianxh

#@Email : 729560832@qq.com

#@File : conf.py

#@Software: PyCharm

import configparser
class Conf(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

