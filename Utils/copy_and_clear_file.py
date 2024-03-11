#-- coding: utf-8 --

#@Time : 2022/7/27 14:29

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : copy_and_clear_file.py

#@Software: PyCharm
from Utils.operationyaml import *
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
def copyfile(f1,f2):
    content=f1.read()
    f2.write(content)
    f1.flush()
    f2.flush()
    f1.close()#关闭文件
    f2.close()
    return

def copyfile_yaml(file1,file2):
    """
    复制文件内容
    :param file1: 原文件
    :param file2: 被复制的文件
    :return:
    """
    if read_yaml_no_key(file1) != None and isinstance(read_yaml_no_key(file1),list):
        file1 = open(file1, mode='r', encoding='utf-8')  # 用读取方式打开test1.txt文本
        file2 = open(file2, mode='w', encoding='utf-8')  # 用写入方式打开test2.txt文本 test2.txt是需要复制的文件夹
        copyfile(file1, file2)
    else:
        pass



def clear_file(file1):
    """
    清空文件内容
    :param file1:文件路径
    :return:
    """
    with open(file1, mode='w', encoding='utf-8') as f:
        f.seek(0)
        f.truncate()
        f.flush()
        f.close()

def copyfile_all(file1,file2):
    """
    复制文件内容
    :param file1: 原文件
    :param file2: 被复制的文件
    :return:
    """

    file1 = open(file1, mode='r', encoding='utf-8')  # 用读取方式打开test1.txt文本
    file2 = open(file2, mode='w', encoding='utf-8')  # 用写入方式打开test2.txt文本 test2.txt是需要复制的文件夹
    copyfile(file1, file2)