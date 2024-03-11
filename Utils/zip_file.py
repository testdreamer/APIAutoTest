#-- coding: utf-8 --

#@Time : 2022/9/15 14:42

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : zip_file.py

#@Software: PyCharm
import os
import zipfile


# 压缩
def make_zip(source_dir, output_filename):
    """
    压缩文件
    :param source_dir: 文件源路径
    :param output_filename: 文件压缩后路径
    :return:
    """
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            print(filename)
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
            zipf.write(pathfile, arcname)
        print()
    zipf.close()


# 解压缩
def un_zip(file_name):
    """
    解压缩文件
    :param file_name: 文件源路径
    :return:
    """
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
        for names in zip_file.namelist():
            zip_file.extract(names, file_name + "_files/")
    zip_file.close()