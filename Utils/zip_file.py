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
    # 在output_filename路径上创建一个空的zip文件，以写入的形式打开
    zipf = zipfile.ZipFile(output_filename, 'w')
    # 获取source_dir的长度
    pre_len = len(os.path.dirname(source_dir))
    # 循环遍历该目录及子目录里面的本身地址，该文件夹中所有目录的名字，该文件夹中所有文件的名字
    for parent, dirnames, filenames in os.walk(source_dir):
        # 再循环遍历获取所有的该文件夹中的文件名字
        for filename in filenames:
            print(filename)
            # 拼接形成所有子目录下的文件的绝对路径
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